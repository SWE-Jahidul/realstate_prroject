# Generated by Django 2.2.4 on 2019-09-02 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20190902_2106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract_details',
            old_name='contruct_info',
            new_name='contruct_informations',
        ),
    ]