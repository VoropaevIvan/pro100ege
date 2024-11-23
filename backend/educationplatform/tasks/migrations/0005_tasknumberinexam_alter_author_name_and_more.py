# Generated by Django 4.2.1 on 2024-10-02 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0004_alter_task_exam"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskNumberInExam",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("slug", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="author",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="difficultylevel",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="tasksource",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="tasktopic",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name="task",
            name="number_in_exam",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="tasks.tasknumberinexam",
            ),
            preserve_default=False,
        ),
    ]