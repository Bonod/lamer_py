# Generated by Django 2.0.1 on 2018-01-21 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milicien', '0002_auto_20180120_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='assistance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromuser', models.IntegerField()),
                ('touser', models.IntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='friend1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='friend2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='checkin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='credits',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
