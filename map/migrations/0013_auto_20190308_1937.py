# Generated by Django 2.1.1 on 2019-03-08 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0012_economia_pop_ocupada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='economia',
            name='pop_ocupada',
            field=models.IntegerField(null=True),
        ),
    ]
