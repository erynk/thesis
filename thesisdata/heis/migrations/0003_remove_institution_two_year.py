# Generated by Django 4.0.2 on 2022-02-06 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heis', '0002_institution_community_college_institution_votech'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='two_year',
        ),
    ]