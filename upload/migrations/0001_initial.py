# Generated by Django 4.2.7 on 2023-11-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]
