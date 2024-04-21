from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from app.serializers import *
from rest_framework import status
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import redirect


class L_Home(APIView):
    def get(self, request):
        if request.user.is_anonymous or (not request.user.is_anonymous and request.user.profile.profession.lower() == 'civilian'):
            return redirect('/login_p')
        else:
            civilian_profiles = Profile.objects.filter(profession__iexact='civilian')
            return render(request, "L_home.html", {'civilian_profiles': civilian_profiles})
    
    def post(self,request):
        pass
        
        
        
class C_Home(APIView):
    def get(self, request):
        if request.user.is_anonymous or (not request.user.is_anonymous and request.user.profile.profession.lower() == 'lawyer'):
            return redirect('/login_p')
        else:
        # Retrieve all profiles with the profession set to 'lawyer'
            lawyer_profiles = Profile.objects.filter(profession__iexact='lawyer')
            return render(request, "C_home.html", {'lawyer_profiles': lawyer_profiles})
    
    def post(self,request):
        pass
            
class Home(APIView):
    def get(self, request):
        return render(request, "home.html")
    
class Create_P(APIView):
    def get(self, request):
        return render(request, "create.html")
    
    def post(self, request):
        data = request.data
        serializers = CreateSerializers(data=data)
        print(data)

        if serializers.is_valid():
            serializers.save()
            return redirect('/login_p/')
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
class Login_P(APIView):
    def get(self, request):
        return render(request, "login.html")
    
    def post(self, request):
        data = request.data
        serializer = LoginSerializers(data=data)
        
        if serializer.is_valid():
            username = serializer.validated_data.get('name')
            password = serializer.validated_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                # Redirect based on user's profession
                if user.profile.profession.lower() == 'civilian':
                    return redirect('/civilian')  # Redirect to civilian view
                elif user.profile.profession.lower() == 'lawyer':
                    return redirect('/lawyer')  # Redirect to lawyer view
                else:
                    return Response("404 Not Found", status=status.HTTP_404_NOT_FOUND)
        print(serializer.errors)
        return Response("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)  
      
class Logout(APIView):
    def get(self, request):
        username = request.user.username if request.user.is_authenticated else None
        logout(request)
        return render(request, 'logout.html', {'username': username})
        