# Generated by Django 4.2.8 on 2023-12-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_list', models.CharField(blank=True, max_length=100)),
                ('todo_detail_view', models.PositiveIntegerField(blank=True)),
                ('todo_create', models.CharField(blank=True, max_length=100)),
                ('todo_update', models.PositiveIntegerField(blank=True)),
                ('todo_delete', models.PositiveIntegerField(blank=True)),
            ],
        ),
    ]
