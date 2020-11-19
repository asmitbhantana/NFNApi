# Generated by Django 3.1.3 on 2020-11-19 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='gender',
            field=models.CharField(choices=[('2', 'Female'), ('3', 'Other'), ('1', 'Male')], max_length=1),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='user_type',
            field=models.CharField(choices=[('2', 'NFN Worker'), ('1', 'User'), ('4', 'NFN Admin'), ('3', 'NFN Leader')], default='1', max_length=1),
        ),
    ]
