# Generated by Django 3.0.3 on 2020-02-12 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200212_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
