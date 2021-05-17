from django.db import models

# Create your models here.

# Table for the car's Manufacturer
class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length=20)

    def __str__(self):
        return self.manufacturer
    

class Car(models.Model):
    car_model = models.CharField(max_length=20)
    banner_main = models.ImageField(upload_to='images/',default='default.png')
    name_of_manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.CharField(max_length=10)
    millage = models.IntegerField()
    description = models.TextField()
    condition = models.CharField(max_length=10)
    banner_image2 = models.ImageField(upload_to='images/',default='default.png')
    banner_image3 = models.ImageField(upload_to='images/',default='default.png')
    banner_image4 = models.ImageField(upload_to='images/',default='default.png')
    banner_image5 = models.ImageField(upload_to='images/',default='default.png')

    def __str__(self):
        return self.car_model
    


