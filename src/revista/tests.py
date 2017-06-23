import pytest
from .models import Revista
from datetime import datetime


def test_criar_revista(db):
    try:
        revista = Revista.objects.create(nome='Natura',
                                         validade="2011-09-01T13:20:30+03:00",
                                         arquivo=None)
        revista.save()
    except Exception:
        assert False
    pass
