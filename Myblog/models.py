from django.conf import settings
from django.db import models
from django.utils import timezone

# Делаем модель нашего БЛога
# НУжно подумать что там нам для этого нужно.
# заглавие
# Текст
# Автор всего это дела
# Дата создания всего это дела
# Дата публикации


# Post
# --------

# title - заглавие
# text - текст
# author - автор
# created_date - Дата создания
# published_date - Дата публикации

# Попробуем написать модель
# эти модели записываются в базу данных db.sqlite3

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# ПОСле создания модели