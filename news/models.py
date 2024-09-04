from django.db import models

# Create your models here
class News(models.Model):
    CATEGORY = {
        'Новость': "Новость",
        'Кружки': "Кружки"
    }
    title = models.CharField('Заголовок', max_length=70)
    full_text = models.TextField('Статья')
    category = models.CharField(max_length=20, choices=CATEGORY)
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title