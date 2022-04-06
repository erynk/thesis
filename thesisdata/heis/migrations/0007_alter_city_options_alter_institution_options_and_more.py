# Generated by Django 4.0.2 on 2022-02-09 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heis', '0006_institution_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ('city',), 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='institution',
            options={'ordering': ('name', 'city')},
        ),
        migrations.AlterField(
            model_name='city',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='heis.region', verbose_name='region'),
        ),
    ]
