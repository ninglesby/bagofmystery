# Generated by Django 3.1.1 on 2020-09-22 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0004_auto_20200922_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='bagcontent',
            name='discarded',
            field=models.BooleanField(default=False),
        ),
    ]
