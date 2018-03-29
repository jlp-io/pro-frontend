# Generated by Django 2.0.2 on 2018-03-29 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NasdaqCompanies',
            fields=[
                ('companyid', models.AutoField(db_column='companyID', primary_key=True, serialize=False)),
                ('symbol', models.CharField(db_column='Symbol', max_length=5)),
                ('name', models.CharField(db_column='Name', max_length=75)),
                ('sector', models.CharField(db_column='Sector', max_length=50)),
            ],
            options={
                'db_table': 'Nasdaq_Companies',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(db_column='userID', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('password', models.CharField(max_length=100)),
                ('salt', models.CharField(max_length=100)),
                ('history', models.TextField(blank=True, null=True)),
                ('favorites', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='SearchUtility',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('prodigal_app.user',),
        ),
    ]
