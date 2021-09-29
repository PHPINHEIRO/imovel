# Generated by Django 3.2.7 on 2021-09-29 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0003_auto_20210929_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='valor_comissao',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Comissao'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='valor_imovel',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor do Imovel'),
        ),
    ]
