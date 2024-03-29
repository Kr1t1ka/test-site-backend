# Generated by Django 3.1.7 on 2021-03-27 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0005_steps_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='название факультета')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='jwt',
        ),
        migrations.AddField(
            model_name='user',
            name='ip',
            field=models.TextField(default='123', verbose_name='ip пользователя'),
        ),
        migrations.AddField(
            model_name='answer',
            name='faculty',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Test.faculty', verbose_name='факультет'),
        ),
    ]
