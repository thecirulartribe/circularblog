# Generated by Django 4.2.15 on 2024-09-02 16:28

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0013_alter_blog_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="content",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Text"
            ),
        ),
    ]
