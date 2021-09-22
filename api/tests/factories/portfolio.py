import factory
from .user import UserFactory
from api.models import Portfolio

class PortfolioFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Portfolio

    title = factory.Faker('text', max_nb_chars=20, locale='ja_JP')
    description = factory.Faker('texts', locale='ja_JP')
    github = factory.Faker('url', locale='ja_JP')
    image = ''
    user = factory.SubFactory(UserFactory)
