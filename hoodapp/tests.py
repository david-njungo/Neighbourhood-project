from django.test import TestCase
from .models import Neighhood
# Create your tests here.
class NeighhoodTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.berkley = Neighhood(neighbourhood_name= 'Berkleyhood',location ='WestCoast',occupantscount =30)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.berkley,Neighhood))

         # Testing Save Method
    def test_save_method(self):
        self.berkley.save_hood()
        hoods = Neighhood.objects.all()
        self.assertTrue(len(hoods) > 0)

    def tearDown(self):
        Neighhood.objects.all().delete()

    def test_get_hoods(self):
        get_hoods= Projects.get_hood()
        self.assertTrue(len(get_hoods)==0)