from django.db import models

class webdata(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    comment=models.CharField(max_length=50)
