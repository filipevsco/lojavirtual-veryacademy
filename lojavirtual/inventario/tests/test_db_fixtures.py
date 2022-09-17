from cgitb import reset
from itertools import count, product
from pydoc import describe
from sqlite3 import IntegrityError
from time import strftime
from unicodedata import category
from unittest import result
from venv import create

import pytest
from lojavirtual.inventario import models


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (18,, on", 1),
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
    "slug, is_active",
    [
        ("fashion", 1),
        ("trainers", 1),
        ("baseball", 1),
    ],
)
def test_inventorio_db_categoria_inserir_dados(
    db, categoria_factory, slug, is_active
):
    result = categoria_factory.create(slug=slug, is_active=is_active)

    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, web_id, name, slug, decription, is_active, created_at, updated_at",
    [
        (
            1, 
            "45425810", 
            "widstar running sneakers", 
            "widstar-running-sneakers",
            "Lorem ipsu, dolor sit amet, consectetur adpiscing elit. Pront porta, eros vel solicita.",
            1, 
            "2021-09-04 22:14:18", 
            "2021-09-04 22:14:18",
        ),
                (
            8616, 
            "45434425", 
            "impact puse dance shoe", 
            "impact-puse-dance-shoe",
            "Loremo nsectetur adpiscing elit. Pront porta, eros vel solicita. asre dois gol abacaxi",
            1, 
            "2021-09-04 22:14:18", 
            "2021-09-04 22:14:18",
        ),
    ],
)
def test_inventario_db_produto_dbfixture(db, django_db_setup, id, web_id, name, slug, decription, is_active, created_at, updated_at):
    result = modes.Produto.objects.get(id=id)
    result_create_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    assert result.web_id == web_id
    assert result.slug == slug
    assert result.description == description
    assert result.is_active == is_active
    assert result.created_at == created_at
    assert result.updated_at == updated_at


def test_inventario_db_produto_uniqueness_integrity(db, product_factory):
    new_web_id = product_factory.create(web_id=123456789)
    with pytest.raises(IntegrityError)
        product_factory.create(web_id=123456789)


@pytest.mark.dbficture
def test_inventory_db_product_insert_data(
    db, product_factory, category_factory
):

    new_category = categorty_factory.create()
    new_product = product_factory.create(category=(1, 36))
    result_product_category = new_product.category.all().count()
    assert "web_id_" in new_product.web_id
