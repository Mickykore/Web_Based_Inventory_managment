# Generated by Django 4.2.1 on 2023-06-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_remove_order_order_by_alter_order_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_by',
            field=models.CharField(choices=[('customer_name', 'Customer'), ('staff', 'Staff')], default='staff', max_length=20),
        ),
    ]
