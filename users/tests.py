from django.test import TestCase
from django.contrib.auth.models import User


def test_create():
    u = User.objects.create(username='testeuse12r', password='1231231231231asc')
    u.delete()
    print('User Test Passed')

test_create()