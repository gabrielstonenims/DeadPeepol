# Generated by Django 3.0.3 on 2020-02-20 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200220_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vtrack',
            old_name='user_album',
            new_name='user_platform',
        ),
    ]
