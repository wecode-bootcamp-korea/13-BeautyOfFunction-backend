# Generated by Django 3.1.3 on 2020-11-11 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='order_item',
        ),
    ]
