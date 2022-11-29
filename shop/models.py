from django.db import models

# Create your models here.
#
class Shop_element(models.Model):
    name_element = models.CharField('Название товара', max_length=100, default='')
    description_element = models.TextField('Описание товара', max_length=250, default='')
    id_element = models.IntegerField('Уникальный id,не должен повторяться', max_length=10)
    #count_element = models.

    def __str__(self):
        return  self.title

    class meta():
        verbose_name = 'Товар'
        verbose_name_Plural = 'Товары'