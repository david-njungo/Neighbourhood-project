from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighhood(models.Model):
    Neighbourhood_name = models.CharField(max_length =30)
    location = models.CharField(max_length =30)
    occupantscount = models.IntegerField(null=True, blank=True)
    admin = models.ForeignKey('User', on_delete=models.CASCADE))

    def __str__(self):
        return self.hoodname
    class Meta:
        ordering = ['hoodname'] 

    def save_hood(self):
        self.save() 

    # @classmethod  
    # def get_project(cls):
    #     projects = cls.objects.all()
    #     return projects
class User(models.Model):
    user_name = models.CharField(max_length=150,blank=True)
    Neighbourhood = models.ForeignKey('Neighhood',on_delete=models.CASCADE)
    email_address = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Business(models.Model):
    business_name = models.CharField(max_length=150,blank=True)
    business_emailaddress = models.EmailField()
    admin = models.ForeignKey('User', on_delete=models.CASCADE))
    Neighbourhood = models.ForeignKey('Neighhood',on_delete=models.CASCADE)
    
