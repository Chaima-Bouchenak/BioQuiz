# Generated by Django 3.1.2 on 2021-10-30 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bioquiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='imageField',
        ),
        migrations.AddField(
            model_name='question',
            name='imageField',
            field=models.ManyToManyField(to='Bioquiz.Image'),
        ),
    ]
