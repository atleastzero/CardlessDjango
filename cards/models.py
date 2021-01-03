from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Card(models.Model):
    card_image = models.ImageField(upload_to='user_cards')
    card_code = models.CharField(max_length=50)
    user_name = models.CharField(max_length=200)
    user_company = models.CharField(max_length=200, blank=True)
    user_title = models.CharField(max_length=200, blank=True)
    user_phone = PhoneNumberField(blank=True)
    user_email = models.EmailField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return user_name + " - " + user_title + " at " + user_company