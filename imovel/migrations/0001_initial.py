# Generated by Django 3.2.7 on 2021-09-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('valor_imovel', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor do Imovel')),
                ('data_inclusao', models.DateField(auto_now_add=True, verbose_name='Data Cadastro')),
                ('tipo', models.CharField(choices=[('APARTAMENTO', 'Apartamento'), ('LOTE', 'Lote')], max_length=11, verbose_name='Tipo')),
                ('status', models.BooleanField(choices=[(True, 'Ativo'), (False, 'Inativo')], verbose_name='Status')),
            ],
            options={
                'ordering': ('descricao', 'valor_imovel'),
            },
        ),
    ]
