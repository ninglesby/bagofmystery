# Generated by Django 3.1.1 on 2020-09-25 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0008_auto_20200922_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bagcontent',
            name='bag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='bag.bag'),
        ),
    ]