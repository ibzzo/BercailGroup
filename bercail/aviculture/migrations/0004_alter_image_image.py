# Generated by Django 4.1 on 2023-06-04 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviculture', '0003_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
