# Generated by Django 4.1 on 2022-08-22 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_test_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
    ]