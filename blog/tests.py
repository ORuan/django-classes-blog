from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


def test_create():
    u = User.objects.get(id=2)
    teste1 = Post.objects.create(title='Teste', content="Teste", author=u)
    teste2 = Post.objects.create(title='Teste 2 asdasd asdasdasda ',
                        content="000000000000000000000000000000000", author=u)
    print('Blog Test Passed')
    teste2.delete()
    teste1.delete()

test_create()