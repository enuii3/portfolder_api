from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


def upload_portfolio_path(instance, filename):
    ext = filename.split('.')[-1]
    return '/'.join(['portfolios', str(instance.title)+str(instance.user.id)+str(".")+str(ext)])


class UserManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not name:
            raise ValueError('name is must')
        if not email:
            raise ValueError('email is must')

        user = self.model(name=name, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, password):
        user = self.create_user(name, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=20, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=50, null=False, blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    title = models.CharField(null=False, blank=False, max_length=35)
    description = models.CharField(null=False, blank=False, max_length=1000)
    github = models.URLField(unique=True, null=False, blank=False)
    image = models.ImageField(null=False, blank=False, upload_to=upload_portfolio_path)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
