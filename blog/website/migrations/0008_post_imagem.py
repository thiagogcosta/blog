# Generated by Django 3.0.2 on 2020-01-19 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_remove_post_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
