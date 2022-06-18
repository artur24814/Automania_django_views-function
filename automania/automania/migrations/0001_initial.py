# Generated by Django 4.0.4 on 2022-04-25 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('stars', models.CharField(choices=[('0', '0'), ('*', '*'), ('**', '**'), ('***', '***'), ('****', '****'), ('*****', '*****')], max_length=64, null=True)),
                ('datetime', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('descriptions', models.TextField()),
                ('telephone', models.DecimalField(decimal_places=0, max_digits=9)),
                ('email', models.EmailField(max_length=254)),
                ('type_order', models.CharField(choices=[('Car', 'Car'), ('AutoParts', 'AutoParts')], max_length=64)),
                ('adress', models.CharField(max_length=128)),
                ('date', models.DateField(auto_now_add=True)),
                ('realized', models.BooleanField(default=False)),
                ('published', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Hatchback', 'Hatchback'), ('Sedan', 'Sedan'), ('SUV', 'SUV'), ('MUV', 'MUV'), ('Crossover', 'Crossover'), ('Coupe', 'Coupe'), ('Convertible', 'Convertible')], max_length=64)),
                ('brand', models.CharField(choices=[('Acura', 'Acura'), ('Alfa-Romeo', 'Alfa-Romeo'), ('Aston-Martin', 'Aston-Martin'), ('Audi', 'Audi'), ('BMW', 'BMW'), ('Chevrolet', 'Chevrolet'), ('Citroen', 'Citroen'), ('Ford', 'Ford'), ('Mazda', 'Mazda'), ('Skoda', 'Skoda'), ('Lexus', 'Lexus'), ('TOYOTA', 'TOYOTA'), ('Nissan', 'Nissan')], max_length=64)),
                ('year', models.IntegerField()),
                ('engine', models.DecimalField(decimal_places=1, max_digits=6)),
                ('car_condition', models.CharField(choices=[('new', 'new'), ('used', 'Used')], max_length=64, null=True)),
                ('country', models.CharField(max_length=64)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('descriptions', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('fuel', models.CharField(choices=[('Gasoline', 'Gasoline'), ('Gas', 'Gas'), ('Diesel', 'Diesel'), ('Electric', 'Electric')], max_length=64, null=True)),
                ('transmission', models.CharField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], max_length=64, null=True)),
                ('damage', models.CharField(choices=[('YES', 'YES'), ('NOT', 'NOT')], max_length=64, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AutoParts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartypes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='automania.cartypes')),
            ],
        ),
    ]
