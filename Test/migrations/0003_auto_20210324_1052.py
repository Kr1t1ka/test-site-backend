# Generated by Django 3.1.7 on 2021-03-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0002_auto_20210324_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.ManyToManyField(to='Test.Answer', verbose_name='вопрос к ответу'),
        ),
    ]
