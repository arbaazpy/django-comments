import random

from django.db import transaction
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from app.models import User, Thread, Club, Comment
from app.factories import (
    UserFactory,
    ThreadFactory,
    ClubFactory,
    CommentFactory
)

NUM_USERS = 50
NUM_CLUBS = 10
NUM_THREADS = 12
COMMENTS_PER_THREAD = 25
USERS_PER_CLUB = 8

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"
ADMIN_EMAIL = "admin@admin.com"


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [User, Thread, Comment, Club]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create all the users
        people = []
        for _ in range(NUM_USERS):
            person = UserFactory()
            people.append(person)

        # Add some users to clubs
        for _ in range(NUM_CLUBS):
            club = ClubFactory()
            members = random.choices(
                people,
                k=USERS_PER_CLUB
            )
            club.user.add(*members)

        # Create all the threads
        for _ in range(NUM_THREADS):
            creator = random.choice(people)
            thread = ThreadFactory(creator=creator)
            # Create comments for each thread
            for _ in range(COMMENTS_PER_THREAD):
                commentor = random.choice(people)
                CommentFactory(
                    user=commentor,
                    thread=thread
                )


        # Create superuser
        user = get_user_model()
        if not user.objects.filter(username=ADMIN_USERNAME, email=ADMIN_EMAIL).exists():
            user.objects.create_superuser(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, email=ADMIN_EMAIL)
            self.stdout.write(f'Local user "{ADMIN_USERNAME}" was created')
