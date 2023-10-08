


from django.urls import path
from . import views

urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('story/<int:pk>/', views.story_detail, name='story_detail'),
    path('app_home/', views.app_home, name='app_home'),
    path('chat_home/', views.chat_home, name='chat_home'),
    path('story_home/', views.story_home, name='story_home'),
    path('story_page_view/', views.story_page_view, name='story_page_view'),
    path('story_view/', views.story_view, name='story_view'),
]

