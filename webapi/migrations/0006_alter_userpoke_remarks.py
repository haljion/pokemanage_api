# Generated by Django 3.2 on 2022-03-09 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0005_auto_20220310_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpoke',
            name='remarks',
            field=models.CharField(blank=True, max_length=300, verbose_name='備考'),
        ),
    ]
