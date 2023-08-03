# Generated by Django 4.2.3 on 2023-08-01 13:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Chat",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=70)),
                (
                    "room",
                    models.CharField(
                        choices=[("books", "books"), ("films", "films"), ("music", "music"), ("games", "games")],
                        max_length=50,
                    ),
                ),
                ("img", models.ImageField(default="default-user-avatar.jpg", null=True, upload_to="chat_img")),
                ("description", models.TextField(blank=True, null=True)),
                ("url", models.CharField(max_length=255, null=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "creator",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
    ]
