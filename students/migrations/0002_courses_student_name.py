# Generated by Django 4.1.2 on 2022-12-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='student_name',
            field=models.CharField(default='ok', max_length=255),
        ),
    ]
