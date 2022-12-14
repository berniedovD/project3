# Generated by Django 4.1.3 on 2022-11-14 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('puzzleID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('puzzleName', models.CharField(max_length=10)),
                ('sudukoString', models.CharField(max_length=81)),
                ('difficultyLevel', models.CharField(choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')], max_length=1)),
                ('newfield', models.CharField(max_length=5)),
            ],
        ),
    ]
