# Generated by Django 3.2.7 on 2021-09-27 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendedor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendedor',
            name='corretora',
        ),
    ]
