# Generated by Django 4.1.3 on 2022-11-30 06:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0018_alter_schooluser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooluser',
            name='terms_conditions',
            field=models.BooleanField(),
        ),
    ]