import pytest
from .models import Revista
from datetime import datetime


class fake_file:
    def __init__(self, my_text):
        self.my_text = my_text

    def readlines(self):
        return self.my_text.splitlines()


def test_criar_revista(db):
    try:
        revista = Revista.objects.create(nome='Natura',
                                         validade="2011-09-01T13:20:30+03:00",
                                         arquivo=None)
        revista.save()
    except Exception:
        assert False
    pass
