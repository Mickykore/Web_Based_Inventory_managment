# Generated by Django 4.2.1 on 2023-06-02 19:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_sales_sale_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='sale_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
