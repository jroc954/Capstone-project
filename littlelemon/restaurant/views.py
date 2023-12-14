from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Menu, Bookingtable
from .serializers import MenuSerializer,BookingtableSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated



# Create your views here.
def index(request):
 return render(request, 'index.html', {})

class MenuView(ListCreateAPIView,):
 
 queryset = Menu.objects.all()
 serializer_class = MenuSerializer

class SingleMenuView(RetrieveUpdateDestroyAPIView):
 queryset = Menu.objects.all()
 serializer_class = MenuSerializer

class bookingtableview(ListCreateAPIView):
 permission_classes = (IsAuthenticated)
 queryset = Bookingtable.objects.all()
 serializer_class = BookingtableSerializer


