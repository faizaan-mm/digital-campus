# Generated by Django 3.1 on 2020-10-02 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineclass', '0005_auto_20201002_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineclass.department'),
        ),
    ]