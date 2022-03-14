from django.db import models

class Product(models.Model):
    title =models.CharField(max_length= 20)
    description =models.TextField()
    price =models.TextField()
    summary =models.TextField(default="All right!")
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)

    def __str__(self):
        return self.title 

