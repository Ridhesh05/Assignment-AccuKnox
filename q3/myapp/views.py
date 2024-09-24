from django.db import transaction
from django.shortcuts import HttpResponse
from .models import Test

def test_signal_transaction(request):
    try:
        with transaction.atomic():
            obj = Test.objects.create(name="Main object")
            print("Main object created.")

            raise Exception("Simulating a failure!")
    except Exception as e:
        print(f"Exception caught: {e}")
    
 
    obj_count = Test.objects.count()
    print(f"Total objects in the database: {obj_count}")

    return HttpResponse(f"Total objects in the database: {obj_count}")
