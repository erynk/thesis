# Generated by Django 4.0.2 on 2022-02-09 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0005_alter_criterion_title_alter_guideline_title_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='criterion',
            options={'ordering': ('id',), 'verbose_name_plural': 'Criteria'},
        ),
        migrations.AlterModelOptions(
            name='guideline',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='principle',
            options={'ordering': ('id',)},
        ),
    ]
