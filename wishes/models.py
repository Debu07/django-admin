from django.db import models

class Wish(models.Model):
    title=models.CharField(max_length=100,blank=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='wishes/images/')
    by=models.CharField(max_length=20,blank=True)
    
    def __str__(self):
        return self.title


