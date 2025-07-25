# Generated by Django 5.2.4 on 2025-07-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singer', '0005_alter_song_singer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='singer',
            name='tags',
            field=models.ManyToManyField(blank=True, to='singer.tag'),
        ),
    ]
