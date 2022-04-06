# Generated by Django 4.0.2 on 2022-02-09 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Principle',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guideline',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
                ('principle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recommendations.principle')),
            ],
        ),
        migrations.CreateModel(
            name='Criterion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
                ('guideline', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recommendations.guideline')),
            ],
            options={
                'verbose_name_plural': 'Criteria',
            },
        ),
    ]