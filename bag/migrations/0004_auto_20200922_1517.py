# Generated by Django 3.1.1 on 2020-09-22 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0003_auto_20200922_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bag',
            name='active_content',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='active', to='bag.bagcontent'),
        ),
    ]