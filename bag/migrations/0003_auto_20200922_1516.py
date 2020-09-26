# Generated by Django 3.1.1 on 2020-09-22 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0002_auto_20200921_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='bag',
            name='active_content',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='is_active', to='bag.bagcontent'),
        ),
        migrations.AlterField(
            model_name='bag',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]