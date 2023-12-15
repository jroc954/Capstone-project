from django.urls import path
from . import views
from .models import Bookingtable, Menu
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token





urlpatterns = [
 path('', views.index, name='index'),
 path('home', views.index, name='home'),
 path('menu/', views.MenuView.as_view()),
 path('menu/<int:pk>', views.SingleMenuView.as_view()),
 path('bookingtable/', views.bookingtableview.as_view()),
 path('api-token-auth/', obtain_auth_token),

 
]