# Generated by Django 3.1.3 on 2020-11-18 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20201118_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='gender',
            field=models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Other')], max_length=1),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='user_type',
            field=models.CharField(choices=[('3', 'NFN Leader'), ('4', 'NFN Admin'), ('2', 'NFN Worker'), ('1', 'User')], default='1', max_length=1),
        ),
    ]