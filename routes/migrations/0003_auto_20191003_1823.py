# Generated by Django 2.0.5 on 2019-10-03 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_auto_20191003_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graph',
            name='weight_edge',
            field=models.CharField(max_length=10),
        ),
    ]
