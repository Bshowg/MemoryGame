# Generated by Django 2.2 on 2020-01-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('points', models.CharField(max_length=50)),
                ('number_of_moves', models.CharField(max_length=50)),
            ],
        ),
    ]
