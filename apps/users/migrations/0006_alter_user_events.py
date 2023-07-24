# Generated by Django 4.2.3 on 2023-07-24 00:31

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='events',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=60), blank=True, max_length=50, size=None),
        ),
    ]
