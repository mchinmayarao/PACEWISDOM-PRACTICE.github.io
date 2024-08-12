from django.shortcuts import render, redirect, HttpResponse
from courses.models import Course, Enrollment
from django.contrib.auth.decorators import login_required
import base64
import json
import requests
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# PayPal API base URL
PAYPAL_API_BASE = "https://api-m.sandbox.paypal.com"
PAYPAL_CLIENT_ID = 'ASMly7o3lAUmGJKP3RVgvi2RR-R42QAzBCXNRtYFsoqL-H0O8SzHUXCMTbRKEplsbcZ9ad36zKlQgzRw'
PAYPAL_CLIENT_SECRET = 'ASMly7o3lAUmGJKP3RVgvi2RR-R42QAzBCXNRtYFsoqL-H0O8SzHUXCMTbRKEplsbcZ9ad36zKlQgzRw'

@login_required(login_url='login')
def checkout(request, *args, **kwargs):
    course_name = kwargs['name']
    course = Course.objects.get(name=course_name)
    
    return render(request, 'checkout.html', {'course': course})


# Generate PayPal Access Token
def generate_access_token():
    auth_string = f"{settings.PAYPAL_CLIENT_ID}:{settings.PAYPAL_CLIENT_SECRET}"
    base64_auth_string = base64.b64encode(auth_string.encode()).decode()

    headers = {
        "Authorization": f"Basic {base64_auth_string}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    body = {
        "grant_type": "client_credentials"
    }

    response = requests.post(f"{PAYPAL_API_BASE}/v1/oauth2/token", headers=headers, data=body)
    response_json = response.json()

    return response_json.get("access_token")


# Handle the API response
def handle_response(response):
    try:
        json_response = response.json()
        return {
            "jsonResponse": json_response,
            "httpStatusCode": response.status_code,
        }
    except ValueError:
        return {
            "jsonResponse": response.text,
            "httpStatusCode": response.status_code,
        }


# Create an order
@csrf_exempt
def create_order(request):
    try:
        # Get the cart data from the request
        course_name = json.loads(request.body).get("course")
        course = Course.objects.get(name=course_name)
        print("Course to buy: ", course)

        access_token = generate_access_token()
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }

        payload = {
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "amount": {
                        "currency_code": "USD",
                        "value": course.price,
                    },
                },
            ],
        }

        response = requests.post(f"{PAYPAL_API_BASE}/v2/checkout/orders", headers=headers, json=payload)
        result = handle_response(response)

        return JsonResponse(result["jsonResponse"], status=result["httpStatusCode"])

    except Exception as e:
        print(f"Failed to create order: {str(e)}")
        return JsonResponse({"error": "Failed to create order."}, status=500)


# Capture an order
@csrf_exempt
def capture_order(request, order_id):
    try:
        access_token = generate_access_token()
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.post(f"{PAYPAL_API_BASE}/v2/checkout/orders/{order_id}/capture", headers=headers)
        result = handle_response(response)
        


        if result["httpStatusCode"] in [200, 201]:  

            transaction = result["jsonResponse"].get("purchase_units", [{}])[0].get("payments", {}).get("captures", [{}])[0]
            
            transaction_id1 = transaction.get("id")
            transaction_id = order_id

            print(transaction_id,transaction_id1)

            request_data = json.loads(request.body)
            course_name = request_data.get("course")
            print("Course Name: ", course_name)
            


            user = request.user
            course = Course.objects.get(name=course_name)
            enrollment, created = Enrollment.objects.get_or_create(
                student=user,
                course=course,
                defaults={'transaction_id': transaction_id}
            )

            if created:
                print("Enrollment Created")
                return JsonResponse({"message": "Payment successful and user enrolled!"}, status=200)
            else:
                print("User Already Enrolled")
                return JsonResponse({"message": "User already enrolled."}, status=200)
        else:
            print("Failed to capture order, HTTP Status: ", result["httpStatusCode"])
            return JsonResponse({"error": "Failed to capture order."}, status=result["httpStatusCode"])

    except Exception as e:
        print(f"Failed to capture order: {str(e)}")
        return JsonResponse({"error": "Failed to capture order."}, status=500)
