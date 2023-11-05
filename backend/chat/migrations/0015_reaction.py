# Generated by Django 4.2.5 on 2023-11-01 17:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0014_alter_message_text"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reaction",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("reaction", models.CharField(max_length=1, null=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("message", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="chat.message")),
                (
                    "user",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
