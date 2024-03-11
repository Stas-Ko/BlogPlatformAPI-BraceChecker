from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(title='Test Title', content='Test Content')

    def test_post_creation(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test Title')
