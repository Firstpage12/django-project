# Generated by Django 4.1.6 on 2023-02-09 14:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("first", "0002_remove_employee_department_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="manager",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name="employee",
            table=None,
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("did", models.CharField(max_length=20)),
                ("dname", models.CharField(max_length=100)),
                (
                    "manager",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="first.employee",
                    ),
                ),
            ],
        ),
    ]
