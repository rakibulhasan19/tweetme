from django.db import models
import random

# Create your models here.
class Tweets (models.Model):
    contant = models.TextField(blank=True,null=True)
    image = models.FileField(upload_to='image/',blank=True,null=True)
    class Meta:
        ordering=['-id']
    def serializ(self):
        return{
            "id":self.id,
            "contant":self.contant,
            "likes": random.randint(0,200)
        }