# Generated by Django 4.2.6 on 2023-11-19 19:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("files", "0001_initial"),
        ("chat", "0015_reaction"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="attachments",
            field=models.ManyToManyField(blank=True, to="files.file"),
        ),
    ]
