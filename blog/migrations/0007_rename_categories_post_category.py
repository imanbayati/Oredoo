# Generated by Django 3.2.13 on 2022-05-29 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categories',
            new_name='category',
        ),
    ]