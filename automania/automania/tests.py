from django.contrib.auth.models import User
from django.test import TestCase

from .models import Car, Messeges


class CarModelTestCase(TestCase):
    def setUp(self):
        user_a = User(username='usr', email='usr@example.com')
        user_a.is_superuser = True
        user_password = 'Password_123'
        self.user_password = user_password
        user_a.set_password(user_password)
        user_a.save()
        self.user_a = user_a

    def test_create_car(self):
        car = Car.objects.create(published=self.user_a,
                                 type='Hatchback',
                                 brand='Acura',
                                 year=2009,
                                 engine=2.1,
                                 country='USA',
                                 descriptions='skhbvefb',
                                 price=10000.00,
                                 fuel='Gasoline',
                                 damage='NOT'
                                 )
        car_count = Car.objects.all().count()
        self.assertEqual(car_count, 1)
        self.assertNotEqual(car_count, 0)

class MessageTestCase(TestCase):
    def setUp(self):
        user_a = User.objects.create_user(username='usr', password='User_password', email='usr@example.com')
        user_b = User.objects.create_user(username='usr1', password='User_password1', email='usr1@example.com')
        self.user_a = user_a
        self.user_b = user_b

    def test_create_message(self):
        message = Messeges.objects.create(from_user=self.user_a, to_user=self.user_b, text="hello")
        message_count = Messeges.objects.all().count()
        self.assertEqual(message_count, 1)
        self.assertNotEqual(message_count, 0)