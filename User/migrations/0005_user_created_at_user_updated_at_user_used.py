# Generated by Django 5.0.7 on 2024-07-14 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_simpleuser_remove_user_used_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='used',
            field=models.IntegerField(default=0),
        ),
    ]
