from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('section/<str:section_name>', views.section, name='section'),
    path('topic/<int:topic_id>', views.topic, name='topic'),
    path('api/get-recent-topic', views.get_recent_topic, name='get_recent_topic'),
    #   path('api/get-hot-topic', views.get_hot_topic, name='get_hot_topic')
]
