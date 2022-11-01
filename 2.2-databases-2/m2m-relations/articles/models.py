from django.db import models


class Tag(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    tags = models.ManyToManyField(Tag, related_name='articles', through='Scope')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-published_at', )


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, verbose_name='Тег', on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        verbose_name = 'Тематика сайта'
        verbose_name_plural = 'Тематики сайта'
