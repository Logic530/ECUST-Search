from django.urls import path
from home.views import IndexView
from users.views import LoginView,RegisterView
app_name='home'
urlpatterns=[
    path('',IndexView.as_view(), name="index"),
    path('login/',LoginView.as_view()),
    path('register/',RegisterView.as_view())
]