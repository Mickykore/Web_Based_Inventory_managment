# Generated by Django 4.2.1 on 2023-06-02 18:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_category_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='sale_date',
            field=models.DateTimeField(default=django.utils.timezone.localtime),
        ),
    ]
