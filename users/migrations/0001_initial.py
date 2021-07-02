# Generated by Django 3.2.4 on 2021-06-25 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('full_name', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=200)),
                ('nick_name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]