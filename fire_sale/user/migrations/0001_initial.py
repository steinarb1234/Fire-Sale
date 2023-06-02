# Generated by Django 4.2.1 on 2023-06-02 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('image', models.CharField(blank=True, default='', max_length=9999)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
                ('href', models.URLField(blank=True, max_length=255, null=True)),
                ('href_parameter', models.CharField(blank=True, max_length=255, null=True)),
                ('datetime', models.DateTimeField()),
                ('seen', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('address', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('zip_code', models.CharField(blank=True, max_length=255)),
                ('bio', models.CharField(blank=True, max_length=9999)),
                ('user_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.userinfo')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.country')),
            ],
        ),
    ]
