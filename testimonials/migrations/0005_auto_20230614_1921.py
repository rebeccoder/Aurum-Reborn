# Generated by Django 3.2.19 on 2023-06-14 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0004_alter_testimonial_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='name',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='title',
            field=models.CharField(default='Default Title', max_length=100),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='rating',
            field=models.IntegerField(),
        ),
    ]