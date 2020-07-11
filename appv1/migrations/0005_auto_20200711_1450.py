# Generated by Django 3.0.7 on 2020-07-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0004_auto_20200710_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='trpgsession',
            name='trpg_session_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='trpgsession',
            name='trpg_session_outline',
            field=models.CharField(blank=True, max_length=1024, verbose_name='セッション概要'),
        ),
    ]
