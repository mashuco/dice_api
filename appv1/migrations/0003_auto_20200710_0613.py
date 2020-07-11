# Generated by Django 3.0.7 on 2020-07-10 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0002_diceroll_twitter_users_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionusers',
            name='character_image',
            field=models.ImageField(blank=True, null=True, upload_to='character_images'),
        ),
        migrations.AddField(
            model_name='sessionusers',
            name='character_name',
            field=models.CharField(default='', max_length=255, verbose_name='キャラ名'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sessionusers',
            name='character_profile',
            field=models.CharField(default='', max_length=255, verbose_name='キャラプロフィール'),
            preserve_default=False,
        ),
    ]