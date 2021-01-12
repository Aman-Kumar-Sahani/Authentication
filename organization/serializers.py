from rest_framework import serializers
from .models import Organization
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self,attr):
#         print(attr)
#         return('yesx')

