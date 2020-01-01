from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.urls import reverse


class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None,
                    is_active=True, is_staff=False, is_admin=False, subscribed=True):
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.subscribed = subscribed
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, username, password=None, subscribed=True):
        user = self.create_user(
            email, username, password=password, is_staff=True, subscribed=subscribed)
        return user

    def create_superuser(self, email, username, password=None, subscribed=True):
        user = self.create_user(email, username, password=password,
                                is_staff=True, is_admin=True, subscribed=subscribed)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',
                              max_length=255, unique=True)
    username = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_shortname(self):
        return self.username

    def get_fullname(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_lable):
        return True

    def get_absolute_url(self):
        return reverse('home')
