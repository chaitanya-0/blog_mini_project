# Generated by Django 4.0.3 on 2022-06-29 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_epic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_class',
            name='subtitle',
            field=models.CharField(default='Placeholder Subtitle', max_length=200),
        ),
        migrations.AlterField(
            model_name='post_class',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
