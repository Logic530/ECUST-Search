from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('section/<str:section_name>', views.section, name='section'),
    path('get-topic', views.get_topic, name='get_topic'),
    path('topic/<int:topic_id>', views.topic, name='topic')
]
