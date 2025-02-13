from django.db import models
from django.utils import timezone

# Create your models here.
# class Games(models.Model):

#     pass

class Games(models.Model):

    home = models.CharField(max_length=50, default='')
    away = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50, default='')
    tip = models.CharField(max_length=40, default='', blank=True )
    time = models.DateTimeField(default=timezone.now)
    odd = models.DecimalField(max_digits=10, decimal_places=3)

    results = models.TextField(blank=True)

    def __str__(self):
        return f'{self.home} {self.away} {self.country}'
        # return self.home, self.away 

class NextGame(models.Model):
    home = models.CharField(max_length=50, default='')
    away = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50, default='')
    time = models.DateTimeField(default=timezone.now)
    odd = models.DecimalField(max_digits=10, decimal_places=3)

    results = models.TextField(blank=True)

    def __str__(self):
        return f'{self.home} {self.away} {self.country}'


class LastWeekGame(models.Model):
    home = models.CharField(max_length=50, default='')
    away = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50, default='')
    time = models.DateTimeField(default=timezone.now)
    odd = models.DecimalField(max_digits=10, decimal_places=3)
    tip = models.CharField(max_length=40, default='', blank=True )

    results = models.TextField(blank=True)

    def __str__(self):
        return f'{self.home} {self.away} {self.country}'
    

class Message(models.Model):
    # username = models.CharField(default="", max_length=50)
    email = models.EmailField(blank=True, default='', unique=True)
    message = models.CharField(default="", max_length=50)

    
class ImageProofs(models.Model):
    image = models.ImageField(upload_to='images/')