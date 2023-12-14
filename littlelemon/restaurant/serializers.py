from rest_framework import serializers
from .models import Bookingtable, Menu
from django.contrib.auth.models import User
from rest_framework  import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class BookingtableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookingtable
        fields = '__all__'
        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
