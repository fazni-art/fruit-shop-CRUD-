from django.db import models

# Create your models here.
class frutables(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField(max_length=300)
    price=models.IntegerField()
    image=models.ImageField(upload_to='fruits/', default='default.jpg')