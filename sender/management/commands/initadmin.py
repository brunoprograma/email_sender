from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = 'testuser'
            email = 'test@admin.com'
            password = 'testpass'
            print('Creating account for %s (%s)' % (username, email))
            User.objects.create_superuser(email=email, username=username, password=password)
        else:
            print('Admin accounts can only be created if no Accounts exists')
