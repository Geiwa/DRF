from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,default=00.00)
    created_at = models.DateTimeField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Product name {self.name}"
    

class Category(models.Model):
     name = models.CharField(max_length=50)
     slug = models.SlugField(max_length=50)

     def __str__(self) -> str:
         return f"Category_name: {self.name}"
    







