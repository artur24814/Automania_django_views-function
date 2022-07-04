from django.db import models

# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# from django.conf import settings
#
# User = settings.AUTH_USER_MODEL

# User = get_user_model()


class Opinion(models.Model):
    STARS = [
        ('0', '0'),
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),
    ]
    name = models.CharField(max_length=64)
    text = models.TextField()
    stars = models.CharField(max_length=64, null=True, choices=STARS)
    datetime = models.DateField(auto_now_add=True)

class Car(models.Model):
    TYPE = [
        ('Hatchback', 'Hatchback'),
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('MUV', 'MUV'),
        ('Crossover', 'Crossover'),
        ('Coupe', 'Coupe'),
        ('Convertible', 'Convertible'),
    ]
    BRAND = [
        ('Acura', 'Acura'),
        ('Alfa-Romeo', 'Alfa-Romeo'),
        ('Aston-Martin', 'Aston-Martin'),
        ('Audi', 'Audi'),
        ('BMW', 'BMW'),
        ('Chevrolet', 'Chevrolet'),
        ('Citroen', 'Citroen'),
        ('Ford', 'Ford'),
        ('Mazda', 'Mazda'),
        ('Skoda', 'Skoda'),
        ('Lexus', 'Lexus'),
        ('TOYOTA','TOYOTA'),
        ('Nissan', 'Nissan'),
    ]
    CONDITION = [
        ('new', 'new'),
        ('used', 'Used'),
    ]
    FUEL = [
        ('Gasoline', 'Gasoline'),
        ('Gas', 'Gas'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
    ]

    type = models.CharField(max_length=64, choices=TYPE)
    brand = models.CharField(max_length=64, choices=BRAND)
    year = models.IntegerField()
    engine = models.DecimalField(max_digits=6, decimal_places=1)
    car_condition = models.CharField(max_length=64, null=True, choices=CONDITION)
    country = models.CharField(max_length=64)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    fuel = models.CharField(max_length=64, null=True, choices=FUEL)
    transmission = models.CharField(max_length=64, null=True, choices=[('Automatic', 'Automatic'),('Manual', 'Manual')])
    damage = models.CharField(max_length=64, null=True, choices=[('YES','YES'), ('NOT', 'NOT')])
    published = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True, null=True)

    def get_url(self):
        return f'/car/{self.id}/'
    def get_update_url(self):
        return f'/update-car/{self.id}'




class CarTypes(models.Model):
    pass

class AutoParts(models.Model):
    pass
    cartypes = models.ForeignKey(CarTypes, null=True, on_delete=models.SET_NULL)

class Order(models.Model):
    TYPE = [
        ('Car', 'Car'),
        ('AutoParts', 'AutoParts'),
    ]
    name = models.CharField(max_length=64)
    descriptions = models.TextField()
    telephone = models.DecimalField(max_digits=9,decimal_places=0)
    email = models.EmailField()
    type_order = models.CharField(max_length=64, choices=TYPE)
    adress = models.CharField(max_length=128)
    published = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=True, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    realized = models.BooleanField(default=False)

    def get_order_url(self):
        return f'/update-order/{self.id}'

class Messeges(models.Model):

    from_user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='+')
    to_user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='+')
    text = models.TextField()
    data = models.DateField(auto_now_add=True)

class ReadedMesseges(models.Model):
    owner = models.CharField(max_length=128)
    message = models.ForeignKey('Messeges', on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    data = models.DateField(auto_now_add=True)
