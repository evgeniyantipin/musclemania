from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория' #название приложения в ед.
        verbose_name_plural = 'Категории' # название мн. числ.

class SubCategory(models.Model):
    parent_category = models.ForeignKey(Category)
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'subcategories'
        verbose_name = 'Подкатегория' #название приложения в ед.
        verbose_name_plural = 'Подкатегории' # название мн. числ.


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    description = models.TextField(blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
