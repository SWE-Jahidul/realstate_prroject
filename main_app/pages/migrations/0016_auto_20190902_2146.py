# Generated by Django 2.2.4 on 2019-09-02 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20190902_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent_details',
            name='our_agents',
        ),
        migrations.RemoveField(
            model_name='agent_details',
            name='our_angets_details',
        ),
        migrations.AddField(
            model_name='contract_details',
            name='our_agents',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='contract_details',
            name='our_angets_details',
            field=models.CharField(default='', max_length=200),
        ),
    ]
