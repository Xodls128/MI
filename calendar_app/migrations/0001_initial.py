# Generated by Django 5.1.1 on 2024-09-07 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecruitmentEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('군별', models.CharField(max_length=100)),
                ('모집분야', models.CharField(max_length=100)),
                ('접수기간', models.CharField(blank=True, max_length=100, null=True)),
                ('일차합격자발표', models.CharField(blank=True, max_length=100, null=True)),
                ('최종합격자발표', models.CharField(blank=True, max_length=100, null=True)),
                ('입영월', models.CharField(blank=True, max_length=100, null=True)),
                ('모집인원', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
