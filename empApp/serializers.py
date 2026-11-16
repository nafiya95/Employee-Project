from rest_framework import views
from empApp.serializers import serializers,empSerializer

class empSerializer(empSerializer):
    class meta:
         model=empSerializer
         fields="__all__"
         