# Generated by Django 4.1.3 on 2022-12-06 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avatar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, default='../static/ProyectoFinalApp/img/profile.png', null=True, upload_to='avatares'),
        ),
    ]