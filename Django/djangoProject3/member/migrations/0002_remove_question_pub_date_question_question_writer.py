# Generated by Django 4.0.4 on 2022-05-24 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='question',
            name='question_writer',
            field=models.CharField(default='blank', max_length=500),
        ),
    ]