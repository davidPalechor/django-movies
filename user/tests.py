from django.contrib.auth.models import User
from django.urls import reverse

from test_plus.test import TestCase


class UserTestCase(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_user(
            username='demodemo',
            password='djangodev',
            is_superuser=True,
        )

    def test_login_required_dashboard(self):
        response = self.get('dashboard')
        self.response_302
        self.assertRedirects(
            response,
            '{}?next=/dashboard/'.format(reverse('user:login'))
        )

        with self.login(username='demodemo', password='djangodev'):
            response = self.get('dashboard')
            self.response_200()
            self.assertTrue('Welcome demodemo' in response.content.decode())
