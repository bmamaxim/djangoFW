# Generated by Django 4.2 on 2024-06-29 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habit", "0003_alter_habit_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="last_try",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="последняя рассылка"
            ),
        ),
    ]
