from django.urls import path
from django.conf.urls import url

from . import views
app_name='bbs'
urlpatterns = [
    path('', views.index, name='index'),
    path('section/<str:section_name>', views.section, name='section'),
    path('topic/<int:topic_id>', views.topic, name='topic'),
    path('api/get-recent-topic', views.get_recent_topic, name='get_recent_topic'),
    #   path('api/get-hot-topic', views.get_hot_topic, name='get_hot_topic'),
    url(r'^accounts/login/$', views.userlogin, name='user_login'),
    url(r'^accounts/signup/$', views.usersignup, name='user_signup'),
    url(r'^accounts/logout$', views.userlogout, name='user_logout')
]
