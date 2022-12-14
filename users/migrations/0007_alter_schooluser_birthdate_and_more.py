# Generated by Django 4.1.3 on 2022-11-23 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_users_code_schooluser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooluser',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schooluser',
            name='local_address',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='schooluser',
            name='permanent_address',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='schooluser',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schooluser',
            name='standard',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schooluser',
            name='subject',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='schooluser',
            name='user_type',
            field=models.CharField(choices=[('T', 'Teacher'), ('S', 'Student')], max_length=5),
        ),
    ]
