# Generated by Django 3.2.7 on 2021-09-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0002_venda_vendedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='valor_comissao',
            field=models.FloatField(verbose_name='Comissao'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='valor_imovel',
            field=models.FloatField(verbose_name='Valor do Imovel'),
        ),
    ]
