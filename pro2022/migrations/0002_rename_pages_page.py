# Generated by Django 3.2.15 on 2022-09-23 12:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pro2022', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pages',
            new_name='Page',
        ),
    ]