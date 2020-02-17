# Generated by Django 3.0.3 on 2020-02-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='intro',
            field=models.CharField(blank=True, default='这家伙很懒，什么也没留下', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]