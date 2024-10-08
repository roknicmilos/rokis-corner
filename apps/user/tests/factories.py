from apps.user.models import Subscriber, User
from factory.django import DjangoModelFactory
from factory import Faker


class SubscriberFactory(DjangoModelFactory):
    class Meta:
        model = Subscriber

    email = Faker("email")
    submission_count = Faker("random_int", min=1, max=3)


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = Faker("email")
    password = Faker("password")

    @classmethod
    def create_staff_user(cls):
        return cls(is_active=True, is_staff=True)

    @classmethod
    def create_superuser(cls):
        return cls(is_active=True, is_staff=True, is_superuser=True)
