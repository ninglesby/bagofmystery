# Generated by Django 3.1.1 on 2020-09-28 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0010_bag_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bag',
            name='active_content',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='active', to='bag.bagcontent'),
        ),
    ]
