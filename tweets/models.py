from django.db import models

# Create your models here.
class Tweets (models.Model):
    contant = models.TextField(blank=True,null=True)
    image = models.FileField(upload_to='image/',blank=True,null=True)