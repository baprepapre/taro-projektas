# Generated by Django 4.1.7 on 2023-04-05 16:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0010_alter_reading_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('card', models.CharField(help_text='Specifinis kortos egzempliorius, gautas būrimo metu', max_length=200, verbose_name='Korta')),
                ('position', models.CharField(help_text='Pozicija, kuria korta iškrito būrimo metu', max_length=10, verbose_name='Kortos pozicija')),
            ],
        ),
    ]
