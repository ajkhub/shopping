# Generated by Django 4.1.4 on 2023-01-11 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_rename_cart_cartitem_carts_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='products',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='carts',
            new_name='cart',
        ),
        migrations.AlterModelTable(
            name='cart',
            table='Cart',
        ),
    ]
