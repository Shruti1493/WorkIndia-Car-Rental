
    
from django.db import models
import uuid

from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email,  password = None, **extra_fields):
        if not username:
            raise ValueError('User must have a username')
        
        if not email:
            raise ValueError("User must have an email address")


        user = self.model(username=username,email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(username, email, password = password, **extra_fields)

class CustomUser(AbstractBaseUser):
    id = models.UUIDField( primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    objects = UserManager()
    
    def __str__(self):
        return f'{self.username} -> {self.email}'

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser





# class Car(models.Model):
#     CATEGORY_CHOICES = [
#         ('SUV', 'SUV'),
#         ('Sedan', 'Sedan'),
#         ('Hatchback', 'Hatchback'),
       
#     ]

#     category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
#     model = models.CharField(max_length=100)
#     number_plate = models.CharField(max_length=20, unique=True)
#     current_city = models.CharField(max_length=100)
#     rent_per_hr = models.DecimalField(max_digits=10, decimal_places=2)
#     is_available = models.BooleanField(default=True)

#     def __str__(self):
#         return f'{self.category} - {self.model}'

# # Rental model
# class Rental(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     origin = models.CharField(max_length=100
