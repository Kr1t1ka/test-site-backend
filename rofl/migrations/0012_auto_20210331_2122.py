# Generated by Django 3.1.7 on 2021-03-31 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rofl', '0011_auto_20210331_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='text_repost',
            field=models.CharField(default='Ваш факультет <django.db.models.fields.CharField>', max_length=1500, verbose_name='Текст для репоста'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='description',
            field=models.CharField(default='Ваш факультет <django.db.models.fields.CharField>', max_length=1500, verbose_name='Текст итога'),
        ),
    ]
