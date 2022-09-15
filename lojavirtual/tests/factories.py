import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

fake = Faker()

from lojavirtual.inventario import models


class CategoriaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Categoria

    name = factory.Sequence(lambda n: "cat_slug_%d" % n)
    slug = fake.lexify(text="cat_slug_??????")


register(CategoriaFactory)
