# Generated by Django 4.1.7 on 2023-03-07 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_alter_status_status_name_alter_task_summary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Полное описание'),
        ),
    ]