# Generated by Django 3.1 on 2020-10-01 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineclass', '0002_auto_20200929_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='credits',
            field=models.IntegerField(),
        ),
    ]