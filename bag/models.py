from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bag(models.Model):
    bag_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class BagContent(models.Model):
    bag_content = models.TextField()
    bag = models.ForeignKey(Bag,on_delete=models.CASCADE)

    def __str__(self):
        min_length = 20
        if len(self.bag_content) > min_length:
            return self.bag_content[:min_length] + "..."
        else:
            return self.bag_content