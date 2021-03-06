from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighhood(models.Model):
    image = models.ImageField(upload_to = 'hoods/')
    neighbourhood_name = models.CharField(max_length =30)
    location = models.CharField(max_length =30)
    occupantscount = models.IntegerField(null=True, blank=True)
    

    def __str__(self):
        return self. neighbourhood_name
    class Meta:
        ordering = ['neighbourhood_name'] 

    def save_hood(self):
        self.save() 

    @classmethod  
    def get_hood(cls):
        hoods = cls.objects.all()
        return hoods

class Profile(models.Model):
    user_name = models.CharField(max_length=150,blank=True)
    Neighbourhood = models.ForeignKey('Neighhood',on_delete=models.CASCADE)
    email_address = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def save_user():
        self.save()

class Business(models.Model):
    business_name = models.CharField(max_length=150,blank=True)
    business_emailaddress = models.EmailField()
    admin = models.ForeignKey('Profile', on_delete=models.CASCADE)
    Neighbourhood = models.ForeignKey('Neighhood',on_delete=models.CASCADE)

    def __str__(self):
        return self.business_name
    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_by_name(cls,search_term):
        business = cls.objects.filter(business_name__icontains=search_term)
        return business
