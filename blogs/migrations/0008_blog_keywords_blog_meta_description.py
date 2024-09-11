# Generated by Django 4.2.15 on 2024-08-08 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0007_alter_blog_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="keywords",
            field=models.CharField(default="keywords", max_length=200),
        ),
        migrations.AddField(
            model_name="blog",
            name="meta_description",
            field=models.CharField(default="description", max_length=300),
        ),
    ]
