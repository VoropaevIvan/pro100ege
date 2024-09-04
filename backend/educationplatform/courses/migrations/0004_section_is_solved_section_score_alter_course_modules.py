# Generated by Django 4.2.1 on 2024-09-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="section",
            name="is_solved",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="section",
            name="score",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="course",
            name="modules",
            field=models.ManyToManyField(
                blank=True, related_name="courses", to="courses.module"
            ),
        ),
    ]