# Generated by Django 2.2 on 2019-04-08 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='is_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='is_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]