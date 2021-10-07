# Generated by Django 3.2.4 on 2021-10-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_product_diseases'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='uses',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='care',
            field=models.TextField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='product',
            name='diseases',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='planting',
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]