# Generated by Django 3.2.19 on 2023-07-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20230727_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='image.jpg', upload_to='product_images/'),
        ),
    ]
