from django.urls import path

from User.views import CreateUserView

app_name = "user"
urlpatterns = [
    path('signup/', CreateUserView.as_view(), name="signup"),
]
