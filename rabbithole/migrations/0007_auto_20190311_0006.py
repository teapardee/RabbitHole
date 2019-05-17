# Generated by Django 2.1.3 on 2019-03-11 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rabbithole', '0006_auto_20190310_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=250)),
                ('sub_cat', models.CharField(max_length=250)),
                ('channel_name', models.CharField(max_length=250)),
                ('upload', models.CharField(max_length=250)),
                ('subscribers', models.CharField(max_length=250)),
                ('viewcount', models.CharField(max_length=250)),
                ('upvotes', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='channel_info',
        ),
    ]
