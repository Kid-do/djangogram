# Generated by Django 4.1.9 on 2023-05-28 06:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="cpation",
        ),
        migrations.AddField(
            model_name="post",
            name="caption",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="comment",
            name="id",
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
        ),
        migrations.AlterField(
            model_name="post",
            name="id",
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
        migrations.AlterField(
            model_name="post",
            name="image_likes",
            field=models.ManyToManyField(blank=True, related_name="post_image_likes", to=settings.AUTH_USER_MODEL),
        ),
    ]
