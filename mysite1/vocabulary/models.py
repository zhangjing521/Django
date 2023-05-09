from django.db import models

# Create your models here.
class WordInfo(models.Model):
    word = models.CharField(max_length=50)
    translate_info = models.CharField(max_length=300)
    extra_info = models.CharField(max_length=300)
    time = models.DateField()
