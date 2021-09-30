from django.db import models

# Create your models here.
class Neighhood(models.Model):
    hoodname = models.CharField(max_length =30)
    location = models.CharField(max_length =30)
    occupantscount = models.CharField(max_length =30)

    def __str__(self):
        return self.hoodname
    class Meta:
        ordering = ['hoodname'] 

   
