# Generated by Django 2.2 on 2019-04-08 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_auto_20190408_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='unique_words',
            field=models.IntegerField(default=0),
        ),
    ]
