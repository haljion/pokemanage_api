# Generated by Django 3.2 on 2022-02-08 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0002_alter_userpoke_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpoke',
            name='trainer',
        ),
        migrations.AddField(
            model_name='userpoke',
            name='user_id',
            field=models.CharField(default='', max_length=300, verbose_name='ユーザーID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userpoke',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]