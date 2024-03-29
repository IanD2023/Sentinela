# Generated by Django 3.0 on 2023-09-30 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MACADRESS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, null=True)),
                ('cpf', models.CharField(max_length=11, null=True)),
                ('mac', models.CharField(max_length=255, null=True)),
                ('matricula', models.CharField(max_length=255, null=True)),
                ('qtd_dispositivos', models.IntegerField(max_length=100, null=True)),
                ('tipo', models.IntegerField(max_length=100)),
                ('data_criacao', models.DateField()),
            ],
            options={
                'db_table': 'mac_addresses',
            },
        ),
    ]
