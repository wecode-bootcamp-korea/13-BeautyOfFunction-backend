# Generated by Django 3.1.3 on 2020-11-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20201109_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fragrance',
            name='fragrance_image',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]
