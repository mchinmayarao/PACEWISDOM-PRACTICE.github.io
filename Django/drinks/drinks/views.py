from .models import Drinks
from .serializers import DrinksSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from rest_framework import status,permissions
from rest_framework.authentication import TokenAuthentication,SessionAuthentication,BasicAuthentication
from rest_framework.authtoken.models import Token
# class DrinksView(APIView):

#     def get(self, request, *args, **kwargs):
#         drinks = Drinks.objects.all() 

#         serializer = DrinksSerializer(drinks,many=True) # use many = True when you have more than 1 objects 
#         print(f'type of serializer data : {type(serializer.data)}')
#         return Response({"data":serializer.data} ,status=status.HTTP_200_OK) 

#     def post(self, request, *args, **kwargs):
#         # print(request.data)
#         serializer = DrinksSerializer(data=request.data)
        
#         # print(serializer.is_valid())
#         # return Response({"response":'done'},status=status.HTTP_200_OK)

#         if serializer.is_valid():
#             print(Drinks.objects.filter(name="strawberry").exists())
#             if Drinks.objects.filter(name=serializer.validated_data['name']).exists():

            
#                 return Response({"response":'item already present'},status=status.HTTP_409_CONFLICT)
#             else:
#                 serializer.save()
#                 return Response({"response":'item added','data':serializer.data},status=status.HTTP_201_CREATED)

# class SingleDrinkView(APIView):


#     def get(self,request,id):
       
#         try:
#             drink = Drinks.objects.get(id=id)
#             return Response(DrinksSerializer(drink).data,status=status.HTTP_200_OK)
        
#         except Drinks.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#     def put(self,request,id):
#         try:
#             drink = Drinks.objects.get(id=id)
#             # print(f'drink.name : {drink.name}\nrequest.data["name"] : {request.data["name"]}')
#             # print(Drinks.objects.get(name=request.data['name']).id)
#             # print(drink)
#             if Drinks.objects.get(name=request.data['name']).id != id: # to check if there drink with same name is already present i.e with other id , if the id is same then the name will be equal itself
#                 return Response({"response":"item with same name exits"},status=status.HTTP_409_CONFLICT)
            
#             else:
#                 serializer = DrinksSerializer(drink,data=request.data) # creating a new searializer object with the updated values
#                 if serializer.is_valid(): # to check the values got is same as expected for the model
#                     serializer.save()
#                     return Response(serializer.data,status=status.HTTP_200_OK)
#                 else:
#                     return Response({'response':'invalid details'},status=status.HTTP_400_BAD_REQUEST)
        
#         except Drinks.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
    
#     def delete(self,request,id):
#         try:
#             drink = Drinks.objects.get(id=id)
#             drink.delete()
#             return Response(status=status.HTTP_200_OK)
#         except Drinks.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
    
    

class DrinksViewSet(ModelViewSet):
    # viewset for CRUD operations on drinks. users can only view the drinks

    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


class UsersViewSet(ModelViewSet):
    # viewset for CRUD operations on users. Only admin can view all users.
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [permissions.IsAdminUser]  
        elif self.request.method == 'POST':
            permission_classes = [permissions.AllowAny]  
        elif self.request.method == 'DELETE' or self.request.method == 'PUT':
            permission_classes = [permissions.IsAuthenticated]  
        

        return [permission() for permission in permission_classes]

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self,request,*args, **kwargs):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            
            token, created = Token.objects.get_or_create(user=user)
            login(request,user)
            
            return Response({'token': token.key,"message":"login successfull"})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,*args, **kwargs):
        logout(request)
        return Response({"message":"logout successfull"},status=status.HTTP_200_OK)

class Current(APIView):
    # View for getting the current user logged in
    def get(self,request):
        print(request.user)
        return Response({"user":str(request.user)},status=status.HTTP_200_OK)