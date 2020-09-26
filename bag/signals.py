from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from . import word_generator

def overwrite_username(sender, instance, **kwargs):
    if instance._state.adding:
        generic_name = word_generator.get_words()
        instance.username = generic_name

pre_save.connect(overwrite_username, sender=User)
    