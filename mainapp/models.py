from django.db import models

# Create your models here.


class Doctor(models.Model):
    full_name = models.CharField(max_length=70)
    specialty = models.CharField(max_length=55)
    image = models.ImageField(upload_to='doctor')
    
    def __str__(self):
        return self.full_name
    
class coment(models.Model):
    bemor_img = models.ImageField(upload_to='bemor')
    ism = models.CharField(max_length=55)
    fikr = models.CharField(max_length=100)
    