# Generated by Django 3.2.13 on 2022-06-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]