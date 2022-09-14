from cgitb import reset

import pytest
from lojavirtual.inventario import models


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashoin", 1),
        (18, "trainers", "trainers", 1),
        (35, "baseball", "baseball", 1),
    ],
)
def test_inventario_categoria_dbfixture(
    db, db_fixture_setup, id, name, slug, is_active
):
    result = models.Categoria.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize(
    "name, slug, is_active",
    [
        ("fashion", "fashoin", 1),
        ("trainers", "trainers", 1),
        ("baseball", "baseball", 1),
    ],
)
def test_inventorio_db_categoria_inserir_dados(
    db, categoria_factory, name, slug, is_active
):
    result = categoria_factory.create(
        name=name, slug=slug, is_active=is_active
    )
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active
