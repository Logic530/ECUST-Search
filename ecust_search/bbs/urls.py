from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('section/<str:section>', views.section, name='section'),
    path('topic/<int:topic_id>', views.topic, name='topic')
]
