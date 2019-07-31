# Generated by Django 2.1.1 on 2019-04-08 20:27

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0013_auto_20190308_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='rodovias',
            fields=[
                ('codigo', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
                ('tipo_pavimento', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='titulos_minerarios',
            name='uso',
            field=models.IntegerField(choices=[(-1, '-------'), (0, 'DADO NÃO CADASTRADO'), (1, 'Artesanato  mineral'), (2, 'Balneoterapia'), (3, 'Brita'), (4, 'Cerâmica vermelha'), (5, 'Construção civil'), (6, 'Corretivo de solo'), (7, 'Energético'), (8, 'Engarrafamento'), (9, 'Fabricação de cal'), (10, 'Fabricação de cimento'), (11, 'Fertilizantes'), (12, 'Gema'), (13, 'Industrial'), (14, 'Insumo agrícola'), (15, 'Metalurgia'), (16, 'Não informado'), (17, 'Ourivesaria'), (18, 'Pedra de coleção'), (19, 'Pedra decorativa'), (20, 'Revestimento')]),
        ),
    ]
