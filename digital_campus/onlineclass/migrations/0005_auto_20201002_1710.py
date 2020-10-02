# Generated by Django 3.1 on 2020-10-02 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineclass', '0004_remove_student_sem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='student',
            name='regno',
        ),
        migrations.AlterField(
            model_name='student',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='onlineclass.section'),
        ),
    ]
