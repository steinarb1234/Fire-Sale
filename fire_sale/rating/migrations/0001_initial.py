# Generated by Django 4.2.1 on 2023-05-30 20:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('rating', models.IntegerField()),
                ('offer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='offer.offer')),
            ],
        ),
    ]
