from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    # host =
    # topic =
    # participation =
    # when we updated the instance
    updated =models.DateTimeField(auto_now=True)
    # when we created the instance
    created = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.name