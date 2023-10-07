from django.shortcuts import render, get_object_or_404
from .models import Story

def story_list(request):
    stories = Story.objects.all()
    return render(request, 'stories/story_list.html', {'stories': stories})

def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    return render(request, 'stories/story_detail.html', {'story': story})
