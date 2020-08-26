from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Person

def person_profile(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(
            user=instance,
            name=instance.username,
        )
        print("Profile created!!")

post_save.connect(person_profile, sender=User)







