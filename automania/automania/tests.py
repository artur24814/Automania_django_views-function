from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from .models import Car, Messeges, ReadedMesseges, Order, Opinion


class ModelTestCase(TestCase):
    """
    tests for all Model in automania application
    """
    def setUp(self):
        user_a = User.objects.create_user(username='usr', password='User_password', email='usr@example.com')
        user_a.is_superuser = True
        self.user_a = user_a
        user_b = User.objects.create_user(username='usr1', password='User_password1', email='usr1@example.com')
        self.user_b = user_b

    def test_opinion(self):
        Opinion.objects.create(name='user_a', text="super", stars='*****')
        opinion_count = Opinion.objects.all().count()
        self.assertEqual(opinion_count, 1)
        self.assertNotEqual(opinion_count, 0)


    def test_create_car(self):
        Car.objects.create(published=self.user_a,
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

    def test_create_and_readed_message_(self):
        message = Messeges.objects.create(from_user=self.user_a, to_user=self.user_b, text="hello")
        ReadedMesseges.objects.create(owner='user_a', message=message)
        message_count = Messeges.objects.all().count()
        readed_message_count = ReadedMesseges.objects.all().count()
        self.assertEqual(message_count, 1)
        self.assertEqual(readed_message_count, 1)
        self.assertNotEqual(message_count, 0)
        self.assertNotEqual(readed_message_count,0)

    def test_order(self):
        Order.objects.create(name="user_a",
                             descriptions='test',
                             telephone=792604091,
                             email="user@example.com",
                             type_order='AutoParts',
                             adress="Warszawa, kelecka 64",
                             published=self.user_a)
        order_count = Order.objects.all().count()
        self.assertEqual(order_count, 1)
        self.assertNotEqual(order_count, 0)

class ViewsTestCase(TestCase):
    """
    tests for all views in automania application
    """
    def setUp(self):
        user_a = User.objects.create_user(username='usr', password='User_password', email='usr@example.com')
        user_a.is_superuser = True
        self.user_a = user_a
        user_b = User.objects.create_user(username='usr1', password='User_password1', email='usr1@example.com')
        self.user_b = user_b
        self.client = Client()
        self.car = Car.objects.create(published=self.user_a,
                           image='https://img.freepik.com/premium-photo/astronaut-outer-open-space-planet-earth-stars-provide-background-erforming-space-planet-earth-sunrise-sunset-our-home-iss-elements-this-image-furnished-by-nasa_150455-16829.jpg?w=2000',
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

    def test_homepage(self):
        response = self.client.get(reverse('homepage'), {'car': 'car'})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "automania/homepage.html")

    def test_car_detail(self):
        response = self.client.get(reverse('car_detail', args=[1]))
        response1 = self.client.get(reverse('car_detail', args=[2]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response1.status_code, 404)
        self.assertTemplateUsed(response, 'automania/car.html')

    def test_search_views(self):
        response = self.client.post(reverse('search_views'),{'search':'Acura'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['cars']), 1)
        self.assertTemplateUsed(response, 'automania/search.html')

    def test_create_car(self):
        response = self.client.get(reverse('create_car'))
        self.assertEqual(response.status_code, 302)

        self.client.force_login(user=self.user_a)
        response_for_login_user = self.client.get(reverse('create_car'))

        self.assertEqual(response_for_login_user.status_code, 200)
        self.assertTemplateUsed(response_for_login_user, 'automania/createCar.html')

    def test_post_create_car(self):
        self.client.login(username='usr', password='User_password')
        response_for_login_user_post = self.client.post(reverse('create_car'), {
            'image':'https://img.freepik.com/premium-photo/astronaut-outer-open-space-planet-earth-stars-provide-background-erforming-space-planet-earth-sunrise-sunset-our-home-iss-elements-this-image-furnished-by-nasa_150455-16829.jpg?w=2000',
            'type': 'Hatchback',
            'brand': 'BMW',
            'year': '2012',
            'engine': '2.1',
            'car_condition': 'new',
            'transmission': 'Automatic',
            'country': 'USA',
            'descriptions': 'skhbvefb',
            'price': '40000.00',
            'fuel': 'Gasoline',
            'damage': 'NOT'
        })
        self.assertEqual(response_for_login_user_post.status_code, 302)
        car_count = Car.objects.all().count()
        self.assertEqual(car_count, 2)

    def test_all_car_(self):
        response = self.client.get(reverse('all_car'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'automania/all_car.html')

    def test_your_posts(self):
        self.client.force_login(user=self.user_a)
        response = self.client.get(reverse('your_posts'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['cars']), 1)
        self.assertTemplateUsed(response, 'automania/your_posts.html')


