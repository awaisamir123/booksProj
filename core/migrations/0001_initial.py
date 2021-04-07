# Generated by Django 3.1.4 on 2021-04-05 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255, verbose_name='First name')),
                ('title', models.CharField(max_length=255, verbose_name='Last name')),
                ('description', models.EmailField(max_length=254)),
                ('field_name', models.ImageField(upload_to='')),
            ],
        ),
    ]
