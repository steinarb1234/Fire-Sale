<<<<<<< HEAD
# Generated by Django 4.2.1 on 2023-05-22 13:13
=======
# Generated by Django 3.2 on 2023-05-22 11:27
>>>>>>> a23aae3af207f6144b1986a89353323b386ca830

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('enail', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('avg_rating', models.FloatField(default=0.0)),
                ('image', models.CharField(max_length=9999)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('bio', models.CharField(max_length=255)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userinfo')),
            ],
        ),
    ]
