from django.db import models

# Create your models here.


class products(models.Model):
    product_id = models.AutoField 
    product_name = models.CharField(max_length=20)
    desc = models.CharField(max_length=300)
    pub_date= models.DateField()

class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=20)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    img = models.ImageField()

    def __str__(self):
        return self.product_name


class Product_details(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=20)  
    category = models.CharField(max_length=20)
    subcategory = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    img = models.ImageField(upload_to='Products2/',default='')

    def __str__(self):
        return self.product_name