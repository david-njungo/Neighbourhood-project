from django.test import TestCase
from .models import Neighhood
# Create your tests here.
class NeighhoodTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.berkley = Neighhood(hoodname= 'Berkleyhood',location ='WestCoast',occupantscount ='2')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.berkley,Neighhood))
