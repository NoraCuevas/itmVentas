# Generated by Django 5.1 on 2024-08-08 18:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clients',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('codigoClt', models.CharField(max_length=100)),
                ('razonSocialClt', models.CharField(max_length=100)),
                ('rfcClt', models.CharField(max_length=100)),
                ('regimenFiscalClt', models.CharField(max_length=100)),
                ('mainTelClt', models.CharField(max_length=100, null=True)),
                ('mainEmailClt', models.EmailField(blank=True, default='', max_length=100, null=True)),
                ('mainCalleyCruzamientosClt', models.CharField(max_length=100, null=True)),
                ('mainNumExtClt', models.CharField(max_length=100, null=True)),
                ('mainNumIntClt', models.CharField(max_length=100, null=True)),
                ('mainCpClt', models.CharField(max_length=100)),
                ('mainAsentamientoClt', models.CharField(max_length=100, null=True)),
                ('mainLocalidadClt', models.CharField(max_length=100, null=True)),
                ('mainMunicipioClt', models.CharField(max_length=100, null=True)),
                ('mainEstadoClt', models.CharField(max_length=100, null=True)),
                ('mainPaisClt', models.CharField(max_length=100, null=True)),
            ],
            options={
                'ordering': ('codigoClt',),
            },
        ),
    ]
