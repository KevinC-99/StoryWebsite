import os
import django
from django.core.management import call_command


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Story_Website.settings')
django.setup()

from stories.models import Story

example_stories = [
    {
        "title": "Story 1 ",
        "content": "Once upon a time, in a land far, far away..."
    },
    {
        "title": "Story 2 ",
        "content": "In the loud city glasgow, something strange was about to happen..."
    },
    {
        "title": "Story 3",
        "content": "University of glasgow students, set off to make an amazing app for morgan stanley"
    }
]

def create_stories():
    for example_story in example_stories:
        Story.objects.create(
            title=example_story["title"],
            content=example_story["content"]
        )

def populate_stories():
    create_stories()
    print('Example stories have been created.')

if __name__ == "__main__":
    populate_stories()



