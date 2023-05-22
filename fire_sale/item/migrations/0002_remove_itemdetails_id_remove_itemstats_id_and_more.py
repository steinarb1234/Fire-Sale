# Generated by Django 4.2.1 on 2023-05-22 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemdetails',
            name='id',
        ),
        migrations.RemoveField(
            model_name='itemstats',
            name='id',
        ),
        migrations.AlterField(
            model_name='itemdetails',
            name='item_stats',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='item.itemstats'),
        ),
        migrations.AlterField(
            model_name='itemstats',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='item.item'),
        ),
    ]
