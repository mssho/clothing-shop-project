from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(unique=True)
    # ToDo: user authentication and abstractBaseUser implementations are needed
    USERNAME_FIELD = 'phone_number'
    def __str__(self) -> str:
        return str(self.phone_number)