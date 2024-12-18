# Generated by Django 4.2.1 on 2024-11-23 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskCollectionSolve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.CharField()),
                ('score', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('task_collection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='taskcollections.taskcollection')),
            ],
        ),
    ]
