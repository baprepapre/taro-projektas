# Generated by Django 4.1.7 on 2023-04-09 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0015_alter_reading_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reading',
            name='type',
            field=models.CharField(help_text='Informacija apie būrimą', max_length=50, null=True, verbose_name='Tipas'),
        ),
        migrations.DeleteModel(
            name='ReadingComment',
        ),
    ]
