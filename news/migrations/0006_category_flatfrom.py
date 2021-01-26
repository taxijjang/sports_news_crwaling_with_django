# Generated by Django 3.0 on 2021-01-26 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_daumnews_navernews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FlatFrom',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'flat_form_list',
                'managed': False,
            },
        ),
    ]