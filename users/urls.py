from django.urls import path
from users.views import SigninView, UserView

urlpatterns = [
    path('/signup', UserView.as_view()),
    path('/signin', SigninView.as_view()),
]