from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator

CITY_CHOICES = (
    ('Chittagong', 'Chittagong'),
    ('Hathazari', 'Hathazari'),
    ('Bandarban', 'Bandarban'),
    ('Dhaka', 'Dhaka'),
    ('Rangamati', 'Rangamati'),
    ('Sitakunda', 'Sitakunda'),
    ('Rajshahi', 'Rajshahi'),
    ('Coxs Bazar', 'Coxs Bazar'),
    ('Feni', 'Feni'), ('Kushtia', 'Kushtia'),
    ('Patiya', 'Patiya'),
    ('Khagrachhari', 'Khagrachhari'),
    ('Rangunia', 'Rangunia'),
    ('Jessore', 'Jessore'),
    ('Savar', 'Savar'),
    ('Fatikchhari', 'Fatikchhari'),
    ('Chandanaish', 'Chandanaish'),
    ('Mirsharai', 'Mirsharai'), ('Mirzapur', 'Mirzapur')
)
DIVISION_CHOICES = (
    ('Chittagong', 'Chittagong'),
    ('Dhaka', 'Dhaka'),
    ('Barisal', 'Barisal'),
    ('Khulna', 'Khulna'),
    ('Mymensingh', 'Mymensingh'),
    ('Rajshahi', 'Rajshahi'),
    ('Rangpur', 'Rangpur'),
    ('Sylhet', 'Sylhet'),
    ('Comilla', 'Comilla')
)
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=7)
    division = models.CharField(choices=DIVISION_CHOICES, max_length=50)
    city = models.CharField(choices=CITY_CHOICES, max_length=50)
    zipcode = models.IntegerField()

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICE = (
    ('p', 'plants'),
    ('s', 'seeds'),
    ('b', 'bouquet'),
    ('f', 'fertilizer'),
    ('a', 'accessories'),
)


class Product(models.Model):
    title = models.CharField(max_length=60)
    price = models.FloatField(max_length=10)
    planting = models.TextField(max_length=10000, blank=True)
    care = models.TextField(max_length=10000, blank=True)
    diseases = models.TextField(max_length=1000, blank=True)
    uses = models.TextField(max_length=1000, blank=True)
    grade = models.CharField(max_length=20)
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=20)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.title)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Cancel', 'Cancel'),
    ('On the way', 'On the way'),
    ('Delivered', 'Delivered'),
    ('Packed', 'Packed'),
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=30, choices=STATUS_CHOICES, default='Pending')
