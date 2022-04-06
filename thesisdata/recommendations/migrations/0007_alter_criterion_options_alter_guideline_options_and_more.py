# Generated by Django 4.0.2 on 2022-02-10 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0006_alter_criterion_options_alter_guideline_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='criterion',
            options={'ordering': ('criteria_id',), 'verbose_name_plural': 'Criteria'},
        ),
        migrations.AlterModelOptions(
            name='guideline',
            options={'ordering': ('guideline_id',)},
        ),
        migrations.AlterModelOptions(
            name='principle',
            options={'ordering': ('principle_id',)},
        ),
        migrations.AddField(
            model_name='criterion',
            name='criteria_id',
            field=models.IntegerField(default=1, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='guideline',
            name='guideline_id',
            field=models.IntegerField(default=1, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='principle',
            name='principle_id',
            field=models.IntegerField(default=1, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='criterion',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='guideline',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='principle',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]