# Generated by Django 4.2.3 on 2023-08-02 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_servicecompany_login_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicecompany',
            old_name='login_data',
            new_name='login_nickname',
        ),
    ]
