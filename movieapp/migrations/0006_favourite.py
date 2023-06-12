# Generated by Django 4.2.2 on 2023-06-12 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0005_alter_comment_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('movie_id', models.CharField(max_length=100)),
                ('movie_title', models.TextField(max_length=500, null=True)),
            ],
        ),
    ]
