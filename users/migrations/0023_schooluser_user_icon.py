# Generated by Django 4.1.3 on 2022-12-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_alter_schooluser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='schooluser',
            name='user_icon',
            field=models.ImageField(default='unknown.png', upload_to='images'),
        ),
    ]