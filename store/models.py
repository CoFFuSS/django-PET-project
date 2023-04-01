from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100,
                            db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')
    availability = models.BooleanField(default=True, verbose_name='Наличие товаров')
    content = models.CharField(max_length=155, verbose_name='Информация')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='slug', null=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    # score
    is_active = models.BooleanField(default=True, verbose_name='Наличие')
    cat = models.ForeignKey(Category, related_name='items', on_delete=models.PROTECT,
                            verbose_name='Категория')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_slug': self.slug})

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'
        ordering = ['id']
