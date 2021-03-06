# Generated by Django 3.1 on 2020-09-29 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineclass', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='campus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='onlineclass.campus'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
