# Generated by Django 4.0.2 on 2022-02-09 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0004_criterion_level_alter_criterion_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criterion',
            name='title',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='guideline',
            name='title',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='principle',
            name='title',
            field=models.CharField(max_length=60, null=True),
        ),
    ]