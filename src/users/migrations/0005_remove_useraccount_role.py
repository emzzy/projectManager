# Generated by Django 5.0.9 on 2025-01-21 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_delete_medicalprofessional_delete_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='role',
        ),
    ]
