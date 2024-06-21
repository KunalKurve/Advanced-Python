from django.db import models

# Create your models here.
from django.db import models  
class Product(models.Model):  
    pid = models.CharField(max_length=20)  
    pname = models.CharField(max_length=100)  
    qty = models.IntegerField(null=True)  
    price = models.FloatField()
    class Meta:  
        db_table = "product"  
