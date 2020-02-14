from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('section/<str:section>', views.section, name='section'),
    path('topic/<int:topic_id>', views.topic, name='topic'),
    path('get-topic', views.get_topic, name='get_topic'),
    url(r'^accounts/login/$', 'views.userlogin', name='user_login'),
    url(r'^accounts/register/$', 'views.userregister', name='user_register'),
    url(r'^accounts/logout$', 'views.userlogout', name='user_logout')
]
