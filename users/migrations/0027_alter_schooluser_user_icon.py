# Generated by Django 4.1.3 on 2022-12-06 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_alter_schooluser_user_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooluser',
            name='user_icon',
            field=models.ImageField(blank=True, upload_to='images/profile-icon'),
        ),
    ]
