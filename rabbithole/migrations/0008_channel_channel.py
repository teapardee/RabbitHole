# Generated by Django 2.1.3 on 2019-03-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rabbithole', '0007_auto_20190311_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='channel',
            field=models.CharField(default='null', max_length=250),
        ),
    ]
