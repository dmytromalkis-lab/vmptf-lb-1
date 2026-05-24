from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    description = models.TextField(blank=True, verbose_name="Опис")

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name="Категорія"
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=255, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата коментування")

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Стаття"
    )

    def __str__(self):
        return f"{self.author} -> {self.article.title}"