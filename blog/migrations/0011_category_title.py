# Generated by Django 3.2.13 on 2022-05-30 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]