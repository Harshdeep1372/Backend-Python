# Generated by Django 4.2.8 on 2023-12-04 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_delete',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='todo',
            name='todo_detail_view',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='todo',
            name='todo_update',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
