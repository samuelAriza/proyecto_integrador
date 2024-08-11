# Generated by Django 5.0.7 on 2024-08-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('totalQuantity', models.IntegerField()),
                ('salePrice', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
