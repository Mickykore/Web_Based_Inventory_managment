# Generated by Django 4.2 on 2023-05-27 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_category_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
