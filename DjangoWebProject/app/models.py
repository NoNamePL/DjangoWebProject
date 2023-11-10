"""
Definition of models.
"""

from tabnanny import verbose
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке")
    # Методы класса:
    def get_absolute_url(self):
        return reverse("blogpost", args=[str(self.id)])
    def __str__(self):
        return self.title
    # Метаданные:
    class Meta:
        db_table = "Posts"
        ordering = ["-posted"]
        verbose_name = "Cтатья блога"
        verbose_name_plural = "Cтатьи блога"

admin.site.register(Blog)

class Comment(models.Model):
    text = models.TextField(verbose_name = "Текст комментарий")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата комментария")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор Комментария")
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья комментария")
    # Методы класса:
    def __str__(self):
        return 'Комментарий %d %s к %s' % (self.id, self.author, self.post)
    # Метаданные:
    class Meta:
        db_table = "Comment"
        ordering = ["-date"]
        verbose_name = "Комментарий к статье блога"
        verbose_name_plural = "Комментарии к статье блога"

admin.site.register(Comment)

class CatalogItem(models.Model):
    title = models.TextField(unique_for_date = "Catalogdate",verbose_name= "Название курса")
    Catalogdate = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата создания")
    description = models.TextField(verbose_name = "Краткое содержание")
    image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке")
    cost = models.IntegerField(default='5000',verbose_name="Стоимость курса")
    # Методы класса:
    
    def get_absolute_url(self):
        return reverse("catalogitem", args=[str(self.id)])
    def __str__(self):
        return self.title
    # Метаданные:
    class Meta:
        db_table = "CatalogItems"
        ordering = ["-Catalogdate"]
        verbose_name = "Элемент каталога"
        verbose_name_plural = "Элемент каталога"

admin.site.register(CatalogItem)

class Backet(models.Model):
    title = models.TextField(unique_for_date = "date",verbose_name= "Название курса")
    text = models.TextField(verbose_name = "Текст комментарий")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата добавления в корзину")
    # cost = models.PositiveIntegerField(default='5000',verbose_name="Стоимость курса",)
    course = models.ForeignKey(CatalogItem,on_delete=models.CASCADE,verbose_name="Курс")
    # author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор Комментария")
    # post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья комментария")
    # Методы класса:
    def __str__(self):
        return 'Корзина %d к %s' % (self.id, self.course)
    # Метаданные:
    class Meta:
        db_table = "Backet"
        ordering = ["-date"]
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

admin.site.register(Backet)
