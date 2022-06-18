from django import forms
from .models import Car, Order, Opinion

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'type',
            'brand',
            'year',
            'engine',
            'fuel',
            'car_condition',
            'country',
            'image',
            'descriptions',
            'price',
            'transmission',
            'damage'
        ]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'name',
            'telephone',
            'email',
            'type_order',
            'descriptions',
            'adress',
        ]

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = [
            'name',
            'text',
            'stars',
        ]


