# Generated by Django 2.2.10 on 2020-04-07 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svapp', '0021_auto_20200407_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]