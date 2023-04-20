from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    title_category = models.CharField("Название", max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Категория блюд"
        verbose_name_plural = "Категории блюд"

    def __str__(self):
        return self.title_category


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.PROTECT)
    title = models.CharField(verbose_name="Название блюд", max_length=200)
    description = RichTextUploadingField('Описание')
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    image = models.ImageField("Фото", upload_to="images/")
    is_active = models.BooleanField("Активный", default=True)

    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Название"
        verbose_name_plural = "Название блюд"

    def __str__(self):
        return self.title