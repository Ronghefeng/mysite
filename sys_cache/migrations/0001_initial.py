# Generated by Django 4.0.6 on 2022-07-30 10:21

from django.db import migrations, models
import django.db.models.deletion
import sys_cache.file_storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(storage=sys_cache.file_storage.ImageFileSystemStorage(), upload_to='shop')),
                ('img_type', models.SmallIntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sys_cache.shop')),
            ],
        ),
    ]