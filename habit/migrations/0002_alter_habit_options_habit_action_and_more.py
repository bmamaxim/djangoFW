# Generated by Django 4.2 on 2024-06-23 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("habit", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="habit",
            options={"verbose_name": "привычка", "verbose_name_plural": "привычки"},
        ),
        migrations.AddField(
            model_name="habit",
            name="action",
            field=models.CharField(
                blank=True,
                help_text="Опишите свою привычку",
                max_length=500,
                null=True,
                verbose_name="Привычки",
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="associated_habit",
            field=models.ForeignKey(
                blank=True,
                help_text="Свяжите привычки",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="habit.habit",
                verbose_name="Связзанная привычка",
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="duration",
            field=models.TimeField(
                blank=True,
                help_text="Время на выполнение",
                null=True,
                verbose_name="Продолжительность",
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="nice_habit",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Выберите приятную привычку",
                null=True,
                verbose_name="Приятная привычка",
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="periodicity",
            field=models.CharField(
                blank=True,
                choices=[
                    ("daily", "Ежедневно"),
                    ("every other days", "Каждые два дня"),
                    ("weekend", "Выходные"),
                ],
                default="daily",
                help_text="Частота выполнения",
                max_length=50,
                null=True,
                verbose_name="Периодичность",
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="place",
            field=models.CharField(
                blank=True,
                help_text="Опишите место выполнения",
                max_length=200,
                null=True,
                verbose_name="Место",
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="publication_sign",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Публикация привычки",
                null=True,
                verbose_name="Признак публикации",
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="reward",
            field=models.CharField(
                blank=True,
                help_text="Награда за выполнение привычки",
                max_length=500,
                null=True,
                verbose_name="Вознаграждение",
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="time",
            field=models.DateTimeField(
                blank=True,
                help_text="Начало выполнения",
                null=True,
                verbose_name="Время",
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
    ]
