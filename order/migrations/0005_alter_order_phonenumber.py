# Generated by Django 5.1.4 on 2025-01-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_alter_cartitems_owner_delete_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phonenumber',
            field=models.IntegerField(),
        ),
    ]
