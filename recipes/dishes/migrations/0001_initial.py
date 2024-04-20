# Generated by Django 5.0.4 on 2024-04-19 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('ingredients', models.TextField(verbose_name='Ingredients')),
                ('recipe', models.TextField(verbose_name='Recipe')),
                ('cooktime', models.IntegerField(verbose_name='Cooktime')),
                ('images', models.FileField(blank=True, upload_to='', verbose_name='Images')),
            ],
        ),
    ]