# Generated by Django 2.2.4 on 2019-09-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_contract_details_company_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='why_we_choose_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chose_topic_title', models.CharField(max_length=100)),
                ('topic_details', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='contract_details',
            name='company_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]