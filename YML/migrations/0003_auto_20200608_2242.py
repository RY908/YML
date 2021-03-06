# Generated by Django 3.0.7 on 2020-06-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YML', '0002_auto_20200605_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='acousticness',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='danceability',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='energy',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='instrumentalness',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='key',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='liveness',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='loudness',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='speechiness',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='tempo',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='time_signature',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='valence',
            field=models.FloatField(default=0, null=True),
        ),
    ]
