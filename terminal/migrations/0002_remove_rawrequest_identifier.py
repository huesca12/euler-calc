# Generated by Django 2.2.12 on 2020-05-03 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rawrequest',
            name='identifier',
        ),
    ]