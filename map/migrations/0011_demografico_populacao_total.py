# Generated by Django 2.1.1 on 2019-03-08 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0010_auto_20190307_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='demografico',
            name='populacao_total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
