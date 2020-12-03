# Generated by Django 3.1.3 on 2020-12-03 12:56

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Other')], max_length=1)),
                ('citizenship_number', models.CharField(max_length=100, unique=True)),
                ('current_address', models.CharField(max_length=100)),
                ('permanent_address', models.CharField(max_length=100)),
                ('fb_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('google_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='', verbose_name='profile-image')),
                ('user_type', models.CharField(choices=[('3', 'NFN Leader'), ('4', 'NFN Admin'), ('1', 'User'), ('2', 'NFN Worker')], default='1', max_length=1)),
                ('total_contribution', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
