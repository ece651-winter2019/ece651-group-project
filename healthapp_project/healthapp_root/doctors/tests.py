from django.test import TestCase
import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4
