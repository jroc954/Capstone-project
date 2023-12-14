from django.test import TestCase
from restaurant.models import Bookingtable, Menu

class BookingtableModelTest(TestCase):
  def test_str_representation(self):
    booking = Bookingtable(name='John Doe', number_of_guests=4, booking_date='2022-01-01')
    self.assertEqual(str(booking), 'John Doe')

class MenuModelTest(TestCase):
  def test_str_representation(self):
    menu_item = Menu(title='Burger', price=9.99, inventory=10)
    self.assertEqual(str(menu_item), 'Burger')

  def test_get_item(self):
    menu_item = Menu(title='Burger', price=9.99, inventory=10)
    self.assertEqual(menu_item.get_item(), 'Burger : 9.99')
