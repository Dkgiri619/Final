# Generated by Django 2.2.10 on 2020-06-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20200614_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='company',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
