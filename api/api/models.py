from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Custom User Manager
# In your models.py file

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, full_name, mobile_number, email, account_number, status, user_type,is_staff,is_trainer,is_superuser, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            full_name=full_name,
            mobile_number=mobile_number,
            email=email,
            account_number=account_number,
            status=status,
            user_type=user_type,
            is_staff=is_staff,
            is_trainer=is_trainer,
            is_superuser= is_superuser
            
        )
        user.is_superuser = is_superuser

        user.is_staff= is_staff
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, mobile_number, email, account_number, status, user_type, password):
        user = self.create_user(
            full_name=full_name,
            mobile_number=mobile_number,
            email=email,
            account_number=account_number,
            status=status,
            user_type=user_type,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Trainer(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=255,unique=True)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    account_number = models.CharField(max_length=20,unique=True)
    status = models.BooleanField(default=True)
    user_type = models.CharField(max_length=20)  # You can use choices for this field

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_trainer= models.BooleanField(default=True)
    is_superuser= models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'account_number'
    REQUIRED_FIELDS = ['mobile_number', 'email',  'status', 'user_type','is_staff']

    def __str__(self):
        return self.full_name


class Department(models.Model):
    department_name = models.CharField(max_length=255)
    department_major = models.CharField(max_length=255,default="Major-default") 

class Trainee(models.Model):
    academic_number = models.BigIntegerField(unique=True)
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Violation(models.Model):
    trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateTimeField()
    violation_type = models.CharField(max_length=255)
    violation_details = models.TextField()
    taken_procedure = models.TextField()
    degree = models.BigIntegerField()
