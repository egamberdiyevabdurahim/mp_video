# Generated by Django 5.0.7 on 2024-07-13 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos/')),
                ('code', models.CharField(max_length=1000, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('created_date', models.DateField()),
                ('language', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('time_of', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='Post.category')),
            ],
        ),
    ]