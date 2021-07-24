from django.test import TestCase
from .models import User

# Create your tests here.
class UserModelTest(TestCase):
    def test_proper_str_format(self):
        usr = User(first_name = "Matthew", last_name = "Cornell")

        self.assertIs(usr.__str__(), "Matthew Cornell")
