# Generated by Django 4.1 on 2022-08-14 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_category_created_category_description_category_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=100, verbose_name='description'),
        ),
    ]