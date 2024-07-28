# Generated by Django 5.0.7 on 2024-07-14 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_user_created_at_user_updated_at_user_used'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='used',
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Poster', 'Poster'), ('User', 'User')], default='User', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='telegram_username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
