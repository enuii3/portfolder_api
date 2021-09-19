import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolder_api.settings')

import django
django.setup()

from faker import Faker
from api.models import User, Portfolio

fake = Faker('ja_JP')


def add_fake_user():
    fake_name = fake.name()
    fake_email = fake.email()
    fake_password = fake.password()

    user = User.objects.get_or_create(name=fake_name, email=fake_email, password=fake_password)[0]
    user.save()
    return user


def populate(n=5):
    for entry in range(n):
        fake_title = fake.text(max_nb_chars=20)
        fake_description = fake.texts()
        fake_github = fake.url()
        fake_user = add_fake_user()

        Portfolio.objects.get_or_create(
            title=fake_title, description=fake_description, github=fake_github, user=fake_user
        )[0]


if __name__ == "__main__":
    populate()
