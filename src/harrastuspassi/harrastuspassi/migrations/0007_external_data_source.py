# Generated by Django 2.2.4 on 2019-10-08 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harrastuspassi', '0006_hobby__created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobby',
            name='data_source',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='External data source'),
        ),
        migrations.AddField(
            model_name='hobby',
            name='origin_id',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='ID in external data source'),
        ),
        migrations.AddField(
            model_name='hobbyevent',
            name='data_source',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='External data source'),
        ),
        migrations.AddField(
            model_name='hobbyevent',
            name='origin_id',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='ID in external data source'),
        ),
        migrations.AddField(
            model_name='location',
            name='data_source',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='External data source'),
        ),
        migrations.AddField(
            model_name='location',
            name='origin_id',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='ID in external data source'),
        ),
        migrations.AddField(
            model_name='organizer',
            name='data_source',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='External data source'),
        ),
        migrations.AddField(
            model_name='organizer',
            name='origin_id',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='ID in external data source'),
        ),
    ]
