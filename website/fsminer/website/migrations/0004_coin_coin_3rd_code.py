# Generated by Django 2.0.5 on 2018-05-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20180524_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='coin_3rd_code',
            field=models.IntegerField(default=1),
        ),
    ]
