# Generated by Django 5.0.7 on 2024-07-13 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_alter_user_telegram_id_alter_user_telegram_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='used',
            field=models.IntegerField(default=0),
        ),
    ]