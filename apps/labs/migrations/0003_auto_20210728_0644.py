# Generated by Django 3.2 on 2021-07-28 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0002_alter_labvisit_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='labvisit',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='labs'),
        ),
        migrations.AlterField(
            model_name='labvisit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='labs'),
        ),
    ]