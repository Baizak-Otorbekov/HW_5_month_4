from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Book(models.Model):
    CHOICES = (
        ("Роман", "Роман"),
        ("Фантазия", "Фантазия"),
        ("Романтика", "Романтика"),
    )
    name = models.CharField(
        max_length=155,
        verbose_name='Имя книги'
    )
    author = models.CharField(max_length=155, verbose_name='Автор')
    description = RichTextField(
        verbose_name='Описание'
    )
    date = models.DateField(verbose_name='Дата выхода')
    type = models.CharField(
        choices=CHOICES,
        max_length=155,
        verbose_name='Тип книги',
        help_text='Тут должен быть жанр книги!'
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    is_active = models.BooleanField(default=False, verbose_name='Активен')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
