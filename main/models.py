from django.db import models


class Item(models.Model):
    slug = models.SlugField('Уникальное название', unique=True)
    title = models.CharField('Название товара', max_length=200)
    image = models.CharField('Фото товара', max_length=50)
    desc = models.TextField('Описание товара')
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title


class Order(models.Model):
    name = models.CharField('Имя клиента', max_length=200)
    surname = models.CharField('Фамилия клиента', max_length=200)
    email = models.CharField('Email', max_length=200)
    phone = models.CharField('Телефон', max_length=200)
    basket = models.TextField('Корзина товаров')

    def __str__(self):
        return self.name + ' ' + self.surname + ' (' + self.phone + ')'
