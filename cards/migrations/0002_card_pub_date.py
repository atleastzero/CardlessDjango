# Generated by Django 3.1.4 on 2021-01-03 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
