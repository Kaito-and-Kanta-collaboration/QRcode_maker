from django.test import TestCase
from django.db.utils import DataError, IntegrityError
from accounts.models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='testuser', password='testuser')

    def setUp(self):
        self.user = User.objects.get(id=1)
    
    def test_can_create_user(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.password, 'testuser')

    def test_can_create_super_user(self):
        super_user = User.objects.create_superuser(username='superuser', password='superuser')
        self.assertIsInstance(super_user, User)
        self.assertEqual(super_user.username, 'superuser')
        self.assertTrue(super_user.is_superuser)

    def test_raises_error_when_username_are_not_duplicate(self):
        error_user = User(username='testuser', password='testuser')
        with self.assertRaises(IntegrityError):
            error_user.save()

    def test_raises_error_when_username_over_50_characters(self):
        user = User(username='a'*51, password='testuser')
        with self.assertRaises(DataError):
            user.save()

    def test_raises_error_when_username_is_empty(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(username='', password='password')

    def test_user_str_is_equal_to_username(self):
        self.assertEqual(str(self.user), self.user.username)
    
    def test_is_active_true_by_default(self):
        self.assertTrue(self.user.is_active)

    def test_is_staff_false_by_default(self):
        self.assertFalse(self.user.is_staff)

    def test_is_superuser_false_by_default(self):
        self.assertFalse(self.user.is_superuser)