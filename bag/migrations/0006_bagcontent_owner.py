# Generated by Django 3.1.1 on 2020-09-22 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bag', '0005_bagcontent_discarded'),
    ]

    operations = [
        migrations.AddField(
            model_name='bagcontent',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
