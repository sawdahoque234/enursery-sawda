# Generated by Django 3.2.4 on 2021-10-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211003_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='care',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('p', 'plants'), ('s', 'seeds'), ('b', 'bouquet'), ('f', 'fertilizer'), ('a', 'accessories')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='diseases',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]