import pytest
from django.contrib.auth.models import User
from django.core.management import call_command

@pytest.fixture
def criar_usuario_admin(django_user_model):
    """
    Retornar usuario admin
    """
    return django_user_model.objects.create_superuser("admin", "a@a.com", "password")

@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    Carregar DB fixtures
    """
    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixture.json")