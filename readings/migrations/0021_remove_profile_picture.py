# Generated by Django 4.1.7 on 2023-04-27 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0020_alter_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='picture',
        ),
    ]