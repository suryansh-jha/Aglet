# Generated by Django 2.1.8 on 2022-02-25 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_product_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ShippingAddress',
        ),
        migrations.RemoveField(
            model_name='product',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='product',
            name='razorpay_payment_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='username',
        ),
        migrations.AddField(
            model_name='productpayment',
            name='ShippingAddress',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.CharField(max_length=100),
        ),
    ]