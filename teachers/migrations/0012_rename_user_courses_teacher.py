# Generated by Django 4.1.2 on 2023-01-04 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0011_alter_courses_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='user',
            new_name='teacher',
        ),
    ]
