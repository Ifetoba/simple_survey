# Generated by Django 5.1.1 on 2024-09-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_login_username_alter_login_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
