from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

class Command(BaseCommand):
    help = "Create a SocialApp entry for Django Allauth"

    def handle(self, *args, **options):
        site, created = Site.objects.get_or_create(id=1, defaults={"domain": "127.0.0.1", "name": "localhost"})

        app, created = SocialApp.objects.get_or_create(
            provider="google",
            name="Google OAuth",
            client_id="your_client_id",
            secret="your_secret_key"
        )
        app.sites.add(site)
        self.stdout.write(self.style.SUCCESS("SocialApp created successfully"))



# To run this code in terminal use ( python manage.py social_app )