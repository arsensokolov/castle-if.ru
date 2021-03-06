# Generated by Django 3.0.1 on 2019-12-20 03:24

import colorfield.fields
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nik_color', colorfield.fields.ColorField(default='#ff0000', max_length=18, verbose_name='цвет ника')),
                ('msg_color', colorfield.fields.ColorField(default='#ff0000', max_length=18, verbose_name='цвет сообщения')),
                ('refresh_time', models.PositiveSmallIntegerField(choices=[(10, 10), (12, 12), (14, 14), (18, 18), (20, 20), (25, 25), (30, 30), (50, 50)], default=14, verbose_name='время обноелния')),
                ('total_lines', models.PositiveSmallIntegerField(choices=[(10, 10), (15, 15), (20, 20), (25, 25), (30, 30), (35, 35)], default=25, verbose_name='число строк')),
                ('show_smiles', models.BooleanField(default=True, verbose_name='показ смайлов')),
                ('js_on', models.BooleanField(default=True, verbose_name='вкл. Java-script')),
                ('show_avatar', models.BooleanField(default=False, help_text='картинка вместо ника', verbose_name='показ аватар')),
                ('icq_uin', models.PositiveIntegerField(blank=True, null=True, verbose_name='ICQ UIN')),
                ('about', models.TextField(blank=True, null=True, verbose_name='немного о себе')),
                ('last_activity', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
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
