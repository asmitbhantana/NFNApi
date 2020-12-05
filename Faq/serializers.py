from rest_framework.serializers import ModelSerializer

from Faq.models import Faq


class FaqSerializer(ModelSerializer):
    class Meta:
        model = Faq
        fields = ["question", "answer", "is_approved","question_user","pk"]

        extra_kwargs = {
            'question_user': {'read_only': True},
            'pk': {'read_only': True}
        }
