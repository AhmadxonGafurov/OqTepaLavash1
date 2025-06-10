from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name='Name')
    image = models.ImageField(upload_to='category',blank=True,null=True)
    status = models.BooleanField(default=True,verbose_name="Status")

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200,verbose_name='Name')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Category',related_name='products')
    image = models.ImageField(upload_to='product',blank=True,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Price')
    status=models.BooleanField(default=True,verbose_name='Status')

    def __str__(self):
        return self.name
class Branche(models.Model):
    name=models.CharField(max_length=200,verbose_name='Name')
    image=models.ImageField(upload_to='brand',blank=True,null=True)
    status=models.BooleanField(default=True,verbose_name='Status')
    address=models.URLField(blank=True,null=True,verbose_name='Address')
    close_open=models.TextField(max_length=120,verbose_name='ish vaqti')
   



    def __str__(self):
        return self.name
    
