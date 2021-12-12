# Generated by Django 3.2.9 on 2021-11-18 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211118_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Bio', models.TextField(max_length=100)),
                ('experience', models.CharField(max_length=50)),
                ('fees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Interior_Designer_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Bio', models.TextField(max_length=100)),
                ('experience', models.CharField(max_length=50)),
                ('fees', models.IntegerField()),
            ],
        ),
    ]
