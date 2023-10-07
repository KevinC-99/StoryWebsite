


from django.urls import path
from . import views

urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('story/<int:pk>/', views.story_detail, name='story_detail'),
]

