from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Test

@receiver(post_save, sender=Test)
def my_model_post_save(sender, instance, **kwargs):
    print(f"Signal triggered for: {instance}")
    
