# Generated by Django 4.1 on 2023-06-10 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviculture', '0004_alter_image_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_commande', models.CharField(max_length=10, unique=True)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=20)),
                ('option', models.CharField(max_length=100)),
                ('commentaire', models.TextField(blank=True)),
            ],
        ),
    ]
