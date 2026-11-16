
import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create or reset the project administrator"

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.environ.get("PROJECT_ADMIN_USERNAME")
        email = os.environ.get("PROJECT_ADMIN_EMAIL")
        password = os.environ.get("PROJECT_ADMIN_PASSWORD")

        if not all([username, email, password]):
            raise CommandError(
                "Admin environment variables are missing."
            )

        user = User.objects.filter(username=username).first()

        if user:
            self.stdout.write("Existing admin account found.")
            user.email = email
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.is_active = True
            user.role = "admin"
            user.save()

            self.stdout.write(
                self.style.SUCCESS(
                    "Administrator password reset successfully."
                )
            )

        else:
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
            )

            user.role = "admin"
            user.save()

            self.stdout.write(
                self.style.SUCCESS(
                    "Administrator created successfully."
                )
            )
