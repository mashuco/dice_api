# Generated by Django 3.0.8 on 2020-09-14 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0006_auto_20200829_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionusers',
            name='character_name',
            field=models.CharField(max_length=20, verbose_name='キャラ名'),
        ),
        migrations.AlterField(
            model_name='sessionusers',
            name='name',
            field=models.CharField(max_length=20, verbose_name='ユーザー名'),
        ),
    ]