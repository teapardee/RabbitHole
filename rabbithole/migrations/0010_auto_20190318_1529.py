# Generated by Django 2.1.3 on 2019-03-18 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rabbithole', '0009_auto_20190317_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel_submissions',
            name='channel_submission',
            field=models.CharField(max_length=250),
        ),
    ]