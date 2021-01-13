from django.db import models


class Articles(models.Model):

    title = models.CharField('Заголовок', max_length=20)
    anons = models.CharField('Анонс новости', max_length=250)
    full_text = models.TextField('Подробное описание')
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
