from django.urls import path

from User.views import CreateUserView, CreateTokenView, working

app_name = "user"
urlpatterns = [
    path('signup/', CreateUserView.as_view(), name="signup"),
    path('login/', CreateTokenView.as_view(), name='login'),
    path('', working, name="working"),

]
