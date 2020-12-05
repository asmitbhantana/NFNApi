from http.client import HTTPResponse

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from Faq.models import Faq
from Faq.serializers import FaqSerializer


class FaqViewSet(viewsets.ModelViewSet):
    serializer_class = FaqSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        current_user = self.request.user
        if current_user.user_type == 'A' \
                or current_user.user_type == 'L':
            return Faq.objects.all()
        else:
            return Faq.objects.filter(is_approved=True)

    def partial_update(self, request, *args, **kwargs):
        faq = Faq.objects.get(pk=self.kwargs["pk"])
        current_user = self.request.user
        if current_user == faq.question_user \
                or current_user.user_type == 'A' \
                or current_user.user_type == 'L':
            try:
                if self.request.data["is_approved"]:
                    faq.is_approved = self.request.data["is_approved"]
                elif self.request.data["answer"]:
                    faq.answer = self.request.data["answer"]
            except MultiValueDictKeyError:
                pass
            faq.save()
            return JsonResponse({"response": "updated faq"}, status=200)
        return JsonResponse({"response": "no string to faq"}, status=400)

    def perform_update(self, serializer):
        faq = Faq.objects.get(pk=self.kwargs.get("pk"))
        faq_user = faq.question_user
        current_user = self.request.user
        if current_user == faq_user \
                or current_user.user_type == 'A' \
                or current_user.user_type == 'L':
            serializer.save()

    def perform_create(self, serializer):
        print(f"on perform_create called {serializer}")
        serializer.save(question_user=self.request.user)

    def perform_destroy(self, instance):
        faq = instance
        print(f"instance is {faq}")
        current_user = self.request.user
        if current_user.user_type == 'A' or current_user.user_type == 'L':
            faq.delete()
            return super(FaqViewSet, self).perform_destroy(instance)
