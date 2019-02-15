from django.db import models

from django.contrib.auth import get_user_model

from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(help_text='in euros')
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Book(Product):
    editor = models.CharField(max_length=50)
    # tags =
    weight = models.PositiveIntegerField()


class EBook(Product):
    editor = models.CharField(max_length=50)
    # tags =
    download_link = models.URLField()


class Cryptocurrency(Product):
    release_date = models.DateField()
    volume = models.PositiveIntegerField()
    historical_maximum = models.PositiveIntegerField()
    historical_minimum = models.PositiveIntegerField()
    weekly_price =  models.PositiveIntegerField()
    monthly_price = models.PositiveIntegerField()
    # graph  =


class Flight(Product):
    FLIGHT_CLASS = (
        ('tourist', 'tourist'),
        ('executive', 'executive'),
        ('first_class', 'first_class'),
    )

    _class = models.CharField(max_length=5, choices=FLIGHT_CLASS)
    source = models.ForeignKey(City, related_name="source_city", on_delete=models.DO_NOTHING)
    destination = models.ForeignKey(City, related_name="destination_city", on_delete=models.DO_NOTHING)
    departure = models.DateTimeField()
    landing = models.DateTimeField()

    # CREAR VALIDADOR QUE EL END SEA POSTERIOR AL START
    # AVISE SI EL DESTINO DEL VUELO


class Hotel(Product):
    HOTEL_RATING = (
        ('disgusting', '**'),
        ('fair', '***'),
        ('good', '****'),
        ('superb', '*****'),
    )

    location = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    rating = models.CharField(max_length=5, choices=HOTEL_RATING)
    acommodation_duration = models.PositiveIntegerField()
    acommodation_start = models.DateTimeField()
    acommodation_end = models.DateTimeField()

    # Precio lo calcule como la duration por el precio por dia
    # Especificar que en el caso del hotel el precio es por dia
    # CREAR VALIDADOR QUE EL END SEA POSTERIOR AL START

class Customer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dni = models.CharField(max_length=10)
    aux_identification = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    address = models.TextField()
    registered = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    interests = models.ManyToManyField(Category)

    # Si dni relleno, el otro campo vacio y viceversa (validador)
    # validador de DNI


class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.DO_NOTHING)
    cart_items = models.ManyToManyField(Product)

    def __str__(self):
        return f"ID:{self.customer__dni}, Person:{self.customer__name} {self.customer__surname}"


class Credit(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"ID:{self.customer__dni}, Person:{self.customer__name} {self.customer__surname}"
