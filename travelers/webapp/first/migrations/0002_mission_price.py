# Generated by Django 3.0.3 on 2020-02-16 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
