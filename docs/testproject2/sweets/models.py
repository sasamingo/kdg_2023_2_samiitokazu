from django.db import models

# Create your models here.
class Sweets(models.Model):
    title = models.CharField(max_length=256)  # タイポを修正しました
    text = models.TextField()
    thumbnail = models.ImageField()

class accounts(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()
