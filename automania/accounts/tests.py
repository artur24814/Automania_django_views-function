from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase

class UserTestCast(TestCase):

    def setUp(self):
        user_a = User(username='usr', email='usr@example.com')
        user_a.is_superuser = True
        user_password = 'Password_123'
        self.user_password = user_password
        user_a.set_password(user_password)
        user_a.save()
        self.user_a = user_a

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    def test_user_password(self):
        self.assertTrue(self.user_a.check_password(self.user_password))

    def test_login_url(self):
        login_url = settings.LOGIN_URL
        data = {'username': self.user_a.username, 'password': self.user_password}
        response = self.client.post(login_url, data, follow=True)
        status_code = response.status_code
        redirect_path = response.request.get("PATH_INFO")
        # self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)
        self.assertEqual(status_code, 200)
