from django.test import TestCase
from accounts.models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='testuser', password='testuser')

    def setUp(self):
        self.user = User.objects.get(id=1)
    


    
