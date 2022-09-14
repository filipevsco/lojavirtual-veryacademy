from tabnanny import verbose

from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Categoria(MPTTModel):
    """
    Tabela Categoria Inventorio implementada com MPTT
    """

    name = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("nome categoria"),
        help_text=_("format: required, max-100"),
    )
    slug = models.SlugField(
        max_length=150,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category safe URL"),
        help_text=_(
            "format: required, letters, numbers, underscore, or hyphens"
        ),
    )
    is_active = models.BooleanField(default=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("parent of categoria"),
        help_text=_("format: not required"),
    )

    class MPPTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("produto categoria")
        verbose_name_plural = _("produto categorias")

    def __str__(self):
        return self.name
