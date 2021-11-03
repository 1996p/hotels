from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Offer(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=28, verbose_name="Название")
    image = models.ImageField(verbose_name="Изображение", blank=True)
    price = models.IntegerField(verbose_name="Цена")
    country = models.CharField(max_length=30, verbose_name="Страна")
    city = models.CharField(max_length=50, verbose_name="Город")
    rating = models.IntegerField(verbose_name="Рейтинг предложения")
    short_description = models.CharField(max_length=3000, verbose_name="Описание предложения")
    slug = models.SlugField(max_length=20, verbose_name='Unique Slug')

class Hotel(Offer):
    staff_rating = models.IntegerField(verbose_name="Рейтинг персонала")
    all_hotel_rooms = models.IntegerField(verbose_name="Всего номеров")
    free_hotel_rooms = models.IntegerField(verbose_name="Количество свободных номеров")
    free_lux_rooms = models.IntegerField(verbose_name="Количество свободных люкс-номеров")
    in_specoffers = models.BooleanField(verbose_name="Находится в списке спецпредложений", default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hotel_detailed', kwargs={'slug': self.slug})

class Review(models.Model):
    username = models.CharField(max_length=50, verbose_name="Имя пользователя")
    content = models.CharField(max_length=1000, verbose_name="Содержимое")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:20]

class OurServices(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название услуги')
    short_description = models.CharField(max_length=100, verbose_name="Краткое описание")
    content = models.CharField(max_length=1000, verbose_name='Описание услуги')
    image = models.ImageField(verbose_name='Изображение')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=20, verbose_name='Service slug')

    def __str__(self):
        return self.title

class RoomTypes(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тип номеря")

    def __str__(self):
        return self.name

class HotelRoom(models.Model):
    type_of_room = models.ForeignKey(RoomTypes, on_delete=models.CASCADE)
    hotel_owner = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return str(self.type_of_room) + " " + str(self.hotel_owner)

class Tours(Offer):

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detailed_tour', kwargs={'slug': self.slug})