# Generated by Django 2.2 on 2020-01-19 16:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboards',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
