# Generated by Django 3.2.5 on 2021-07-30 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210730_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewpost',
            name='age',
        ),
        migrations.RemoveField(
            model_name='viewpost',
            name='img',
        ),
    ]
