# Generated by Django 4.1.7 on 2023-04-03 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0003_arcana_suit_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='id',
            field=models.IntegerField(help_text='Kortos seka kaladėje', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(help_text='Kortos pavadinimas', max_length=100, verbose_name='Pavadinimas'),
        ),
    ]
