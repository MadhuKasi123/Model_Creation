# Generated by Django 4.2.7 on 2023-12-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_topicname_topic_topic_name_webpage_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='url',
            field=models.URLField(max_length=100),
        ),
    ]
