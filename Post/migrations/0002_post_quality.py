# Generated by Django 5.0.7 on 2024-07-13 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='quality',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
