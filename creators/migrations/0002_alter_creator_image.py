# Generated by Django 3.2.19 on 2023-07-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creators', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='image',
            field=models.ImageField(default='default_image.jpg',
                                    upload_to='creators/'),
        ),
    ]
