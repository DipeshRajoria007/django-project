# Generated by Django 4.2.9 on 2024-01-27 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default=':LASJFD_@#$(PDPFIJODS', max_length=32),
            preserve_default=False,
        ),
    ]
