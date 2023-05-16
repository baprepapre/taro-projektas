# Generated by Django 4.1.7 on 2023-04-05 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0011_cardinstance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='arcana',
            field=models.CharField(choices=[('minor', 'Mažieji arkanai'), ('major', 'Didieji arkanai')], help_text='Pasirinkite arkanus', max_length=5, null=True, verbose_name='Arkanai'),
        ),
        migrations.AlterField(
            model_name='card',
            name='suit',
            field=models.CharField(blank=True, choices=[('none', 'Nėra'), ('wands', 'Lazdos'), ('cups', 'Taurės'), ('swords', 'Kardai'), ('pentacles', 'Monetos')], help_text='Pasirinkite rūšį', max_length=9, null=True, verbose_name='Rūšis'),
        ),
        migrations.DeleteModel(
            name='Arcana',
        ),
        migrations.DeleteModel(
            name='Suit',
        ),
    ]
