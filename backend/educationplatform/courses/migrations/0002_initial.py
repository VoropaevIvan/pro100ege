# Generated by Django 4.2.1 on 2024-11-23 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionsolve',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='section',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tasks.task'),
        ),
        migrations.AddField(
            model_name='section',
            name='theory_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='courses.theorysection'),
        ),
        migrations.AddField(
            model_name='module',
            name='lessons',
            field=models.ManyToManyField(blank=True, to='courses.lesson'),
        ),
        migrations.AddField(
            model_name='lessonsection',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.lesson'),
        ),
        migrations.AddField(
            model_name='lessonsection',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.section'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='section',
            field=models.ManyToManyField(blank=True, related_name='lessons', through='courses.LessonSection', to='courses.section'),
        ),
        migrations.AddField(
            model_name='course',
            name='modules',
            field=models.ManyToManyField(blank=True, related_name='courses', to='courses.module'),
        ),
        migrations.AddField(
            model_name='course',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]