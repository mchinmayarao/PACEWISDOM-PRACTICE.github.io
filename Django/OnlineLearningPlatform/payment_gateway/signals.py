from django.db.models.signals import post_init
from django.dispatch import receiver
from .models import Payment
from courses.models import Course, Enrollment
from users.models import User 
import datetime
from rest_framework.response import Response
from rest_framework import status

@receiver(post_init, sender=Payment)
def handle_payment_status_change(sender, instance, **kwargs):
    payment = instance
    try:
        user = User.objects.get(email=payment.billing_email)
    except User.DoesNotExist:
        print(f"User with email {payment.billing_email} does not exist.")
        return {"payment_status":"error"}

    if payment.status == 'confirmed':
        course = Course.objects.get(name=payment.course)
        if not Enrollment.objects.filter(course=course, student=user).exists():
            Enrollment.objects.create(
                enrolled_at=datetime.datetime.now(),
                student=user,
                course=course,
                transaction_id=payment.transaction_id
            )
        return {"payment_status":payment.status}

    else:
        print(f"Payment {payment.id} is {payment.status}.")
        return {"payment_status":payment.status}
    
