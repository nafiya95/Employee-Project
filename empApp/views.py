from django.shortcuts import render
from rest_framework import views
from rest_framework.views import APIView
from empApp import views
from rest_framework.response import Response
from empApp.serializers import empSerializer
from rest_framework import serializers
from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework import authentication,permissions
from django.contrib.auth.models import User

# Create your views here.


class EmployeeCreateView(APIView,CreateAPIView):
    serializer_class=empSerializer
    def perform_create(self, serializer):
        print(serializer)
        return User.objects.create_user(**serializer.validated_data)
    

class EmployeeUpdateRetrieveDeleteView(UpdateAPIView,RetrieveAPIView,DestroyAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def create(self,serializer):
        print(serializer)
        queryset=User.objects.all()
        self.lookup_url_kwarg="emp_name"

    def create(serializer):
        print("=============")
        fields=['emp_name','emp_email','department','designation','joining_date']
        return User.objects.all()

    




    
    