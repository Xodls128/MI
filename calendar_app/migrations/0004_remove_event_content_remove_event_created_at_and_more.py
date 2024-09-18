# Generated by Django 5.1.1 on 2024-09-17 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0003_event_color_event_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='content',
        ),
        migrations.RemoveField(
            model_name='event',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='event',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='event',
            name='announcement_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
