# Generated by Django 2.2.1 on 2019-05-21 17:58

from django.db import migrations, models
import storage.models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20190520_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfilemodel',
            name='deadline',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='uploadedfilemodel',
            name='file',
            field=models.FileField(upload_to=storage.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='uploadedfilemodel',
            name='upload_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]