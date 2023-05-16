# Generated by Django 4.1.7 on 2023-04-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0005_alter_card_arcana_alter_card_suit_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='readings',
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='profile_pictures/default.jpg', upload_to='profile_pictures'),
        ),
    ]