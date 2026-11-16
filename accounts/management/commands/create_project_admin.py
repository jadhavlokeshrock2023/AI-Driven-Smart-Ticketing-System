
import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create the project administrator"

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.environ.get("PROJECT_ADMIN_USERNAME")
        email = os.environ.get("PROJECT_ADMIN_EMAIL")
        password = os.environ.get("PROJECT_ADMIN_PASSWORD")

        if not all([username, email, password]):
            raise CommandError("Admin environment variables are missing.")

        if User.objects.filter(username=username).exists():
            raise CommandError("Admin username already exists.")

        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )

        user.role = "admin"
        user.save(update_fields=["role"])

        self.stdout.write(
            self.style.SUCCESS("Administrator created successfully.")
        )
