from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

def create_customer(sender, instance, created, **kwargs):
    print("Signal handler started")
    for i in range(5):
        print(f"Signal processing step {i + 1}")
    print("Signal handler finished")

class Customer(models.Model):
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=32)

post_save.connect(create_customer, sender=Customer)
