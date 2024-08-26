from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


# class UserCustomModelManager(BaseUserManager):
#     def create_user(self, email, username, first_name, last_name, password=None, **extra_fields):
#         if not email or not username or not first_name or not last_name:
#             raise ValueError('Users must have email, username, first_name, and last_name fields')
#
#         email = self.normalize_email(email)
#         user = self.model(email_address=email, username=username,
#                           first_name=first_name, last_name=last_name,
#                           **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, username, first_name, last_name, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#
#         if extra_fields.get('is_active') is not True:
#             raise ValueError('Superuser must have is_active=True.')
#
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         user = self.create_user(email, username, first_name, last_name, password=password, **extra_fields)
#         return user


class UserCustomModelManager(BaseUserManager):
    def _create_user(self, email, username, first_name, last_name, password=None, **extra_fields):
        if not email or not username or not first_name or not last_name:
            raise ValueError('Users must have email, username, first_name, and last_name fields')

        email = self.normalize_email(email)
        # email_address
        user = self.model(email=email, username=username,
                          first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')
        return self._create_user(email, username, first_name, last_name, password, **extra_fields)

    def create_superuser(self, email, username, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')
        return self._create_user(email, username, first_name, last_name, password, **extra_fields)


class UserCustomModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True, null=False, blank=False,
                                error_messages={'unique': 'A user with that username already exists.'},
                                default='username', verbose_name='username')
    first_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='First Name',
                                  error_messages={'unique': 'A user with that first name already exists.'})
    last_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Last Name',
                                  error_messages={'unique': 'A user with that last name already exists.'})
    email = models.EmailField(unique=True, null=False, blank=False, default='email@example.com',
                                      error_messages={'unique': 'A user with that email already exists.'},
                                      verbose_name='Email Address')
    phone_number = models.CharField(max_length=11, unique=True, null=False, blank=False, default='79013855268',
                                    error_messages={'unique': 'A user with that phone number already exists.'},
                                    verbose_name='Phone Number')
    date_birth = models.DateField(null=False, blank=False, default=timezone.now,
                                  error_messages={'unique': 'A user with that date birth already exists.'})
    account_created = models.DateTimeField(auto_now_add=True, verbose_name='Account Created',
                                           error_messages={'unique': 'A user with that date created account already exists.'})

    is_active = models.BooleanField(default=True, verbose_name='Is Active?')
    is_staff = models.BooleanField(default=False, verbose_name='Is Staff?')
    is_superuser = models.BooleanField(default=False, verbose_name='Is Superuser?')

    objects = UserCustomModelManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        message = f'id {self.id} {self.first_name} {self.last_name} - username: {self.username}, email: {self.email} | joined: {self.account_created}'
        return message

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['account_created']
        indexes = [
            models.Index(fields=['account_created'])
        ]
