from django.core.management import BaseCommand

from authentication.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(username='admin', email='admin@mail.ru', is_superuser=True, is_staff=True)
        user.set_password('admin')
        user.save()