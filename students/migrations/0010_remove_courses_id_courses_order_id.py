# Generated by Django 4.1.2 on 2022-12-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_rename_standard_courses_student_standard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='id',
        ),
        migrations.AddField(
            model_name='courses',
            name='order_id',
            field=models.AutoField(default=4, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
