# Generated by Django 2.1.1 on 2019-04-08 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0015_auto_20190408_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rodovias',
            name='tipo_pavimento',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
