# Generated by Django 2.1.1 on 2019-03-08 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0011_demografico_populacao_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='economia',
            name='pop_ocupada',
            field=models.FloatField(null=True),
        ),
    ]
