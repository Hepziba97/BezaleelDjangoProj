# Generated by Django 4.0.5 on 2022-06-09 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=230)),
                ('completed', models.CharField(max_length=230)),
            ],
        ),
    ]
