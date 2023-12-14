from django.db import models

# Create your models here.
class Bookingtable(models.Model):
    name = models.CharField(max_length=100)
    number_of_guests = models.IntegerField(null=False)
    booking_date = models.DateField()
    def __str__(self):
        return self.name
    
class Menu(models.Model):
   title = models.CharField(max_length=200) 
   price = models.DecimalField(max_digits=6, decimal_places=2)
   inventory = models.IntegerField(null=False)

   def __str__(self):
      return self.name   