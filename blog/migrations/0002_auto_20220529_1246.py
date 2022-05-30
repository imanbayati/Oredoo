# Generated by Django 3.2.13 on 2022-05-29 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_date']},
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='blog/empty.jpg', upload_to='blog/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(null=True),
        ),
    ]