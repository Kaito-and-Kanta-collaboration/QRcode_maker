from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import User


class UserLoginViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='test')
        user.set_password('testpassword')
        user.save()

    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertTemplateUsed(response, 'accounts/accounts_login.html')

    def test_user_can_login(self):
        response = self.client.post(reverse('accounts:login'), {
                                    'username': 'test', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)

    def test_view_redirect_home_page_after_login(self):
        response = self.client.post(reverse('accounts:login'), {
                                    'username': 'test', 'password': 'testpassword'}, follow=True)
        self.assertTemplateUsed(response, 'home.html')

    def test_authenticated_user_redirect_to_home_page(self):
        _ = self.client.post(reverse('accounts:login'), {
                             'username': 'test', 'password': 'testpassword'}, follow=True)
        response = self.client.get(reverse('accounts:login'), follow=True)
        self.assertTemplateUsed(response, 'home.html')

    def test_view_redirect_login_page_if_user_not_found(self):
        response = self.client.post(reverse('accounts:login'), {
                                    'username': 'nofound', 'password': 'nofound'}, follow=True)
        self.assertTemplateUsed(response, 'accounts/accounts_login.html')


class UserLogoutViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='test')
        user.set_password('testpassword')
        user.save()

    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 302)

    def test_user_can_logout(self):
        _ = self.client.post(reverse('accounts:login'), {
                             'username': 'test', 'password': 'testpassword'})
        response = self.client.get(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 302)

    def test_redirect_to_login_page_after_logout(self):
        _ = self.client.post(reverse('accounts:login'), {
                             'username': 'test', 'password': 'testpassword'})
        response = self.client.get(reverse('accounts:logout'), follow=True)
        self.assertTemplateUsed(response, 'accounts/accounts_login.html')


class UserSignupViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='test')
        user.set_password('testpassword')
        user.save()

    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertTemplateUsed(response, 'accounts/accounts_signup.html')

    def test_can_create_new_account(self):
        before_count = User.objects.all().count
        response = self.client.post(reverse('accounts:signup'), {
                                    'username': 'newuser', 'password': 'newuserpd', 'confirm_password': 'newuserpd'
                                    })
        after_count = User.objects.all().count
        self.assertNotEqual(before_count, after_count)
        self.assertEqual(response.status_code, 302)
    
    def test_authenticated_user_redirect_to_home_page(self):
        _ = self.client.post(reverse('accounts:login'), {'username': 'test', 'password': 'testpassword'})
        response = self.client.get(reverse('accounts:signup'), follow=True)
        self.assertTemplateUsed(response, 'home.html')

    def test_render_signup_page_if_form_is_invalid(self):
        response = self.client.post(reverse('accounts:signup'), {'username': 'test', 'password': 'testpassword'})
        self.assertTemplateUsed(response, 'accounts/accounts_signup.html')