# Generated by Django 5.1.4 on 2025-01-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_remove_order_delete_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phonenumber',
            field=models.IntegerField(default=0),
        ),
    ]
