from django.db import models

# Create your models here.

class destination(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    img = models.ImageField(upload_to='img')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    days = models.IntegerField()
    nights = models.IntegerField()
    like = models.BooleanField(default=False)


    def __str__(self):
        return self.name



