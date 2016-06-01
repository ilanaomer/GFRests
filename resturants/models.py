from django.db import models
from django.core.validators import RegexValidator
import geocoder


# Create your models here.

# ilanaTODO: move to infrastructure
class PhoneValidator(RegexValidator):
    regex = r'^\+?1?\d{9,15}$'
    message = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    about = models.TextField()
    phone_number = models.CharField(max_length=15, validators=[PhoneValidator()],
                                    blank=True)  # validators should be a list
    web_site = models.URLField(blank=True, null=True)
    is_kosher = models.BooleanField(default=False)
    gf_agreement = models.BooleanField(default=False)
    # ilanaTODO missing security
    logo = models.ImageField(upload_to="resturants/", blank=True, null=True)
    COST_LEVEL = (
        ('CHEAP', '$'),
        ('AVERAGE', '$$'),
        ('EXPENSIVE', '$$$'),
    )
    cost_level = models.CharField(max_length=3, choices=COST_LEVEL, default='$$')

    def __str__(self):
        return self.name

    def city(self):
        g = geocoder.google(self.address, language='he')
        return g.city
