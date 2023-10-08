from django.shortcuts import render, get_object_or_404
from .models import Story

def story_list(request):
    stories = Story.objects.all()
    return render(request, 'stories/story_list.html', {'stories': stories})

def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    return render(request, 'stories/story_detail.html', {'story': story})

def app_home(request):
    # Add your app home logic here
    return render(request, 'app_home.html')

def chat_home(request):
    # Add your chat home logic here
    return render(request, 'chat_home.html')

def story_home(request):
    # Add your story home logic here
    return render(request, 'story_home.html')

def story_page_view(request):
    # Add your story page view logic here
    return render(request, 'story_page_view.html')

def story_view(request):
    # Add your story view logic here
    return render(request, 'story_view.html')