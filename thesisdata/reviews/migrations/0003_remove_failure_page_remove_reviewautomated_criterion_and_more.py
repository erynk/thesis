# Generated by Django 4.0.2 on 2022-02-27 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0009_criterion_new21_guideline_new21'),
        ('heis', '0008_alter_page_title'),
        ('reviews', '0002_remove_reviewautomated_failure_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='failure',
            name='page',
        ),
        migrations.RemoveField(
            model_name='reviewautomated',
            name='criterion',
        ),
        migrations.RemoveField(
            model_name='reviewautomated',
            name='page',
        ),
        migrations.RemoveField(
            model_name='reviewautomated',
            name='total_failures',
        ),
        migrations.RemoveField(
            model_name='failure',
            name='criterion',
        ),
        migrations.AddField(
            model_name='failure',
            name='criterion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recommendations.criterion'),
        ),
        migrations.AlterField(
            model_name='reviewautomated',
            name='date_reviewed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reviewautomated',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='heis.institution'),
        ),
        migrations.AlterField(
            model_name='reviewautomated',
            name='tool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.tool'),
        ),
        migrations.CreateModel(
            name='ReviewPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='heis.page')),
                ('review', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.reviewautomated')),
            ],
        ),
        migrations.AddField(
            model_name='failure',
            name='review_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.reviewpage'),
        ),
    ]