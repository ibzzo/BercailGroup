# Generated by Django 4.1 on 2023-06-04 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviculture', '0002_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='static/aviculture/images/'),
        ),
    ]
