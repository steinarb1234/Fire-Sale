# Generated by Django 4.2.1 on 2023-05-28 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='ItemConditions',
            fields=[
                ('condition', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ItemStats',
            fields=[
                ('views', models.IntegerField(default=0)),
                ('watchers', models.IntegerField(default=0)),
                ('status', models.CharField(default='Not sold', max_length=255)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='item.item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(blank=True, max_length=999)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemDetails',
            fields=[
                ('description', models.CharField(blank=True, max_length=9999)),
                ('item_stats', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='item.itemstats')),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='item.itemconditions')),
            ],
        ),
    ]
