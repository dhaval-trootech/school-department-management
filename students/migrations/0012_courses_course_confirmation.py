# Generated by Django 4.1.2 on 2022-12-20 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_rename_price_courses_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_confirmation',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]