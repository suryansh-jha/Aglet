# Generated by Django 2.1.8 on 2022-02-25 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_productpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ShippingAddress',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.FloatField(),
        ),
    ]
