# Generated by Django 3.2 on 2021-07-28 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labvisit',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='labs'),
        ),
    ]