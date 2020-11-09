# Generated by Django 3.1.3 on 2020-11-08 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='gender',
            field=models.CharField(choices=[('2', 'Female'), ('1', 'Male'), ('3', 'Other')], max_length=1),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='user_type',
            field=models.CharField(choices=[('4', 'NFN Admin'), ('3', 'NFN Leader'), ('2', 'NFN Worker'), ('1', 'User')], max_length=1),
        ),
    ]
