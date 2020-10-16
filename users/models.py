from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email, fullname, prodi, status, is_staff, is_active, password, **extra_fields):

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email,
                          fullname=fullname,
                          prodi=prodi,
                          status=status,
                          is_staff=is_staff,
                          is_active=is_active,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self,  email, fullname, prodi, status, is_staff, is_active, password=None, **extra_fields):
        return self._create_user(email, fullname, prodi, status, is_staff, True, password, **extra_fields)

    def create_superuser(self, email, fullname, prodi, status, is_staff, is_active, password=None, **extra_fields):
        return self._create_user(email, fullname, prodi, "Admin", True, True, password,  **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    STATUS_USER = (
        ('Admin', 'Admin'),
        ('FM', 'FM'),
        ('PS', 'PS'),
    )
    created_on = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=255, unique=True)
    fullname = models.CharField(max_length=255)
    # Prodi ini harusnya Foreign Key ke model Prodi
    prodi = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=255, choices=STATUS_USER, blank=True, null=True, default='Admin')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', 'status', 'prodi', 'is_active', 'is_staff']

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super().save(*args, **kwargs)

    def __str__(self):
        return '{} / {}'.format(self.fullname, self.email)