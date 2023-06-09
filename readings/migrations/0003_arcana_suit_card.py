# Generated by Django 4.1.7 on 2023-04-03 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0002_reading_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arcana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('minor', 'Mažieji arkanai'), ('major', 'Didieji arkanai')], help_text='Pasirinkite arkanus', max_length=5, verbose_name='Arkanai')),
            ],
            options={
                'verbose_name': 'Arkanai',
                'verbose_name_plural': 'Arkanai',
            },
        ),
        migrations.CreateModel(
            name='Suit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('none', 'Nėra'), ('wands', 'Lazdos'), ('cups', 'Taurės'), ('swords', 'Kardai'), ('pentacles', 'Monetos')], help_text='Pasirinkite rūšį', max_length=9)),
            ],
            options={
                'verbose_name': 'Rūšis',
                'verbose_name_plural': 'Rūšys',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Įveskite kortos pavadinimą', max_length=100, verbose_name='Pavadinimas')),
                ('description', models.TextField(help_text='Išsamus simbolizmo ir reikšmės aprašymas', max_length=2000, verbose_name='Aprašymas')),
                ('meaning', models.TextField(help_text='Trumpas pagrindinių kortos reikšmių apibūdinimas', max_length=1000, verbose_name='Reikšmė')),
                ('r_meaning', models.TextField(help_text='Trumpas pagrindinių apverstos kortos reikšmių apibūdinimas', max_length=1000, verbose_name='Reikšmė - apversta')),
                ('arcana', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cards', to='readings.arcana')),
                ('suit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cards', to='readings.suit')),
            ],
        ),
    ]
