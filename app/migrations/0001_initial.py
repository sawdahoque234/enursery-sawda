# Generated by Django 3.2.4 on 2021-09-16 16:11

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
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=7)),
                ('city', models.CharField(choices=[('Chittagong', 'Chittagong'), ('Hathazari', 'Hathazari'), ('Bandarban', 'Bandarban'), ('Dhaka', 'Dhaka'), ('Rangamati', 'Rangamati'), ('Sitakunda', 'Sitakunda'), ('Rajshahi', 'Rajshahi'), ('Coxs Bazar', 'Coxs Bazar'), ('Feni', 'Feni'), ('Kushtia', 'Kushtia'), ('Patiya', 'Patiya'), ('Khagrachhari', 'Khagrachhari'), ('Rangunia', 'Rangunia'), ('Jessore', 'Jessore'), ('Savar', 'Savar'), ('Fatikchhari', 'Fatikchhari'), ('Chandanaish', 'Chandanaish'), ('Mirsharai', 'Mirsharai'), ('Mirzapur', 'Mirzapur')], max_length=50)),
                ('division', models.CharField(choices=[('Chittagong', 'Chittagong'), ('Dhaka', 'Dhaka'), ('Barisal', 'Barisal'), ('Khulna', 'Khulna'), ('Mymensingh', 'Mymensingh'), ('Rajshahi', 'Rajshahi'), ('Rangpur', 'Rangpur'), ('Sylhet', 'Sylhet'), ('Comilla', 'Comilla')], max_length=50)),
                ('zipcode', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('price', models.FloatField(max_length=10)),
                ('description', models.TextField(max_length=300)),
                ('brand', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('p', 'plant'), ('s', 'seed'), ('b', 'boquet'), ('f', 'fertilizer'), ('a', 'accessories')], max_length=20)),
                ('product_image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('On the way', 'On the way'), ('Delivered', 'Delivered'), ('Packed', 'Packed')], default='Pending', max_length=30)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
