# Generated by Django 3.0.2 on 2020-01-18 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='sub',
            new_name='sub_title',
        ),
    ]
