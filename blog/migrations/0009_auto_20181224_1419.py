# Generated by Django 2.0 on 2018-12-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20181223_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='last_updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blogtype',
            name='type_name',
            field=models.CharField(max_length=15),
        ),
    ]
