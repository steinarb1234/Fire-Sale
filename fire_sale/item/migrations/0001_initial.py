# Generated by Django 4.2.1 on 2023-05-22 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('category', '0001_initial'),
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
            name='ItemStats',
            fields=[
                ('views', models.IntegerField(default=0)),
                ('watchers', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=255)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='item.item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=9999)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemDetails',
            fields=[
                ('condition', models.CharField(default='noItem', max_length=255)),
                ('description', models.CharField(blank=True, default='noItem', max_length=9999)),
                ('item_stats', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='item.itemstats')),
            ],
        ),
    ]
