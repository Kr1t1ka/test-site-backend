# Generated by Django 3.1.7 on 2021-03-24 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rofl', '0003_auto_20210324_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='answer',
        ),
    ]
