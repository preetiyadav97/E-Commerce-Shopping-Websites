# Generated by Django 4.2.5 on 2023-09-12 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Buy', '0008_cart_created_at_cart_product_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product_qty',
        ),
    ]
