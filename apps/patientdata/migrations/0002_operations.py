# Generated by Django 3.2 on 2021-07-29 08:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patientdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('opdate', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('followup', models.CharField(blank=True, max_length=150, null=True)),
                ('improve', models.CharField(blank=True, max_length=150, null=True)),
                ('heal', models.BooleanField(default=False)),
                ('remark', models.CharField(blank=True, max_length=300, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientdata.patients')),
            ],
        ),
    ]
