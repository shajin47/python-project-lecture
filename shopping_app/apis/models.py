from django.db import models

# Create your models here.


class Products(models.Model):
    Product_Name = models.CharField(max_length=100,blank=False)
    HSN_Code = models.IntegerField(blank=False, unique=True)
    Cost_Price = models.DecimalField(decimal_places=2, max_digits=10)
    Selling_Price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return "%s" % (self.Product_Name)  
