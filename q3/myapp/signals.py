from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import Test

@receiver(post_save, sender=Test)
def create_related_instance(sender, instance, **kwargs):
    print("Signal triggered, creating a related object.")
    Test.objects.create(name=f"Related to {instance.name}")
    print("Related object created.")
