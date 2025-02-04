# Generated by Django 5.1.4 on 2025-01-17 16:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('order', '0003_alter_cart_orderstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderstatus', models.IntegerField(choices=[(1, 'Oroder Processed'), (2, 'DELIVERED'), (3, 'REJECTED'), (4, 'Order Conformed')], default=0)),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=100)),
                ('delete_status', models.IntegerField(choices=[(1, 'live'), (0, 'delete')], default=1)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='customer.customer')),
            ],
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added', to='order.order'),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
