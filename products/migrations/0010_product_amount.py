# Generated by Django 2.1.5 on 2022-02-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20220213_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.CharField(default=100, max_length=100),
            preserve_default=False,
        ),
    ]