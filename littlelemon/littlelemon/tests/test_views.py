from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu, Bookingtable
from restaurant.serializers import MenuSerializer, BookingtableSerializer

class MenuViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_url = reverse('menu-list')
        self.menu_data = {'name': 'Pizza', 'price': 10.99}  # Example menu data

    def test_create_menu(self):
        response = self.client.post(self.menu_url, self.menu_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 1)
        self.assertEqual(Menu.objects.get().name, 'Pizza')

    def test_get_menu_list(self):
        response = self.client.get(self.menu_url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

class BookingtableViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.bookingtable_url = reverse('bookingtable-list')
        self.bookingtable_data = {'name': 'John Doe', 'table_number': 1}  # Example booking table data

    def test_create_bookingtable(self):
        response = self.client.post(self.bookingtable_url, self.bookingtable_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bookingtable.objects.count(), 1)
        self.assertEqual(Bookingtable.objects.get().name, 'John Doe')

    def test_get_bookingtable_list(self):
        response = self.client.get(self.bookingtable_url)
        bookingtables = Bookingtable.objects.all()
        serializer = BookingtableSerializer(bookingtables, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
