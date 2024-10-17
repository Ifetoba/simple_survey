from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.


class Login(models.Model):
    # Add the username field, No default here
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    # Store hashed passwords in a real scenario
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username  # or whatever you want as the string representation


@receiver(pre_save, sender=Login)
def set_default_username(sender, instance, **kwargs):
    if not instance.username:  # Check If the username is empty
        try:
            # Count the number of users already in the Login table, Get the count of existing users to create a default username
            user_count = Login.objects.count() + 1
        except ObjectDoesNotExist:
            # In the case the tbale does not exist yet, set default user_count
            user_count = 1

        instance.username = f"default_user{user_count}"
