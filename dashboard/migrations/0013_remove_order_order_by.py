# Generated by Django 4.2.1 on 2023-06-09 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_order_order_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_by',
        ),
    ]
