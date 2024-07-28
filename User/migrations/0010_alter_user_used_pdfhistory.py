# Generated by Django 5.0.7 on 2024-07-18 22:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_remove_user_telegram_id_account_hiddenhistory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='used',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='PDFHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.FileField(upload_to='pdf_img/')),
                ('file', models.FileField(blank=True, null=True, upload_to='pdfs/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pdf_history', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]