from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Address(models.Model):
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address_details = models.TextField()
    postal_code = models.CharField(validators=[RegexValidator(
        regex=r"\b(?!(\d)\1{3})[13-9]{4}[1346-9][013-9]{5}\b", message="Input postal code is not valid")])
    # This is only for the user, helping not to mistake multiple addresses
    address_name = models.CharField(max_length=50)
    # In case the customer doesn't want to receive the package themselves (optional)
    receiver_name = models.CharField(max_length=50, null=True, blank=True)
    receiver_phone_number = models.CharField(max_length=10, null=True, blank=True)


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    # ToDo: add user here