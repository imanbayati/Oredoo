# Generated by Django 3.2.13 on 2022-06-05 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]