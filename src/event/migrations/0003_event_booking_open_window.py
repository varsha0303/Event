# Generated by Django 4.2.2 on 2023-06-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_booking_booking_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='booking_open_window',
            field=models.IntegerField(default=1, verbose_name='Booking Open Window'),
        ),
    ]
