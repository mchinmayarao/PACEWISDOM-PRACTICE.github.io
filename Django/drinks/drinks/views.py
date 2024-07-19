from django.http import JsonResponse
from .models import Drinks
from .serializers import DrinksSerializer
from django.views import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView




class DrinksView(APIView):

    def get(self, request, *args, **kwargs):
        drinks = Drinks.objects.all() 

        serializer = DrinksSerializer(drinks,many=True) # use many = True when you have more than 1 objects 
        print(f'type of serializer data : {type(serializer.data)}')
        return JsonResponse({"data":serializer.data} ) 

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = DrinksSerializer(data=request.data)
        
        # print(serializer.is_valid())
        # return Response({"response":'done'},status=status.HTTP_200_OK)

        if serializer.is_valid():
            print(Drinks.objects.filter(name="strawberry").exists())
            if Drinks.objects.filter(name=serializer.validated_data['name']).exists():

            
                return Response({"response":'item already present'},status=status.HTTP_200_OK)
            else:
                serializer.save()
                return Response({"response":'item added'},status=status.HTTP_200_OK)

            

        



