from rest_framework import status,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from payments import get_payment_model
from payments.dummy import DummyProvider
from courses.models import Course, Enrollment
import datetime
from .signals import handle_payment_status_change
import time
import random
class InitiatePaymentView(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def post(self, request, *args, **kwargs):
        course_name = request.data.get('course')
        student = request.user
        course = get_object_or_404(Course, name=course_name)

        try:
            e = Enrollment.objects.get(course=course,student=student)
            return Response({"message":"Already enrolled"},status=status.HTTP_208_ALREADY_REPORTED)
       
        except Enrollment.DoesNotExist:
        
            transaction_id = f'TXN{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}{course.name[:2].upper()}{student.name[:3].upper()}'

            Payment = get_payment_model()
            payment = Payment.objects.create(
                variant='dummy', 
                transaction_id=transaction_id,
                currency="USD",
                billing_first_name=request.user.name,
                billing_email=request.user.email,
                description=f"Payment for {course.name}",
                total=course.price,
                course=course.name
            )
            
            # random payment selection and simulating delay 
            randomPayment = random.choice(["waiting","confirmed","rejected","error"])
            print(randomPayment)
            time.sleep(5)
            payment.status = randomPayment

            
            payment_status = handle_payment_status_change(Payment,payment)
            
            return Response(payment_status,status=status.HTTP_200_OK)

