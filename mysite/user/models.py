from django.db import models
from django.contrib.auth.models import \
    AbstractBaseUser, BaseUserManager, PermissionsMixin


class VJUserManager(BaseUserManager):
    def create_user(self, userid, name, phone_number, grade, password, email=None):
        user = self.model(
            userid = userid,
            name = name,
            phone_number = phone_number,
            grade = grade,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, userid, name, phone_number, grade, password, email=None):
        user = self.create_user(
            userid,
            name,
            phone_number,
            grade,
            email,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user


class VJUser(AbstractBaseUser, PermissionsMixin):
    userid = models.CharField(max_length=50, unique=True)
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    grade = models.IntegerField()

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    is_facebook_user = models.BooleanField(default=False)

    USERNAME_FIELD = 'userid'
    REQUIRED_FIELDS = ['name', 'phone_number', 'grade']

    objects = VJUserManager()

    def get_short_name(self):
        return self.name

    @property
    def is_staff(self):
        return self.is_admin
