# Generated by Django 4.1.7 on 2023-04-03 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('readings', '0004_alter_card_id_alter_card_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='arcana',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='card', to='readings.arcana'),
        ),
        migrations.AlterField(
            model_name='card',
            name='suit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='card', to='readings.suit'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('readings', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reading', to='readings.reading')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
