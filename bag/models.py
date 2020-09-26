from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bag(models.Model):
    owner = models.ForeignKey(User, related_name='bags', on_delete=models.CASCADE)
    active_content = models.ForeignKey('BagContent', related_name='active', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=64, unique=True)
    counter = models.IntegerField(default=0)
    @property
    def discarded_count(self):
        return BagContent.objects.filter(bag=self).filter(discarded=True).count()

    def pull_item(self):
        if self.active_content:
            bc = self.active_content
            bc.discarded=True
            bc.save()
            
        self.active_content = BagContent.objects.filter(bag=self).filter(discarded=False).order_by('?').first()
        self.save()
    
    def discard_item(self):
        if self.active_content:
            bc = self.active_content
            bc.discarded=True
            bc.save()
        self.active_content = None
        self.save()

    def put_item_back(self):
        if self.active_content:
            bc = self.active_content
            bc.discarded = False
            bc.save()
        self.active_content = None
        self.save()
    def empty_bag(self):
        self.put_item_back()
        for content in self.contents.all():
            content.delete()
            
    def restore_items(self):
        for content in self.contents.all():
            content.discarded = False
            content.save()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs): 
        self.counter += 1
        super(Bag, self).save(*args, **kwargs) 

class BagContent(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bag_content = models.TextField()
    bag = models.ForeignKey(Bag, related_name='contents', on_delete=models.CASCADE)
    discarded = models.BooleanField(default=False)

    def __str__(self):
        min_length = 20
        if len(self.bag_content) > min_length:
            return self.bag_content[:min_length] + "..."
        else:
            return self.bag_content