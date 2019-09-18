# Generated by Django 2.2.4 on 2019-09-03 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_auto_20190903_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_page_defaut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledership_title', models.CharField(max_length=100)),
                ('ledershi_details', models.CharField(max_length=100)),
                ('ask_question_titlle', models.CharField(max_length=100)),
                ('as_question_details', models.CharField(max_length=300)),
                ('company_contract', models.CharField(max_length=100)),
                ('company_contract_details', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ledership_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leader_ship_agent_name', models.CharField(max_length=100)),
                ('leader_ship_agent_type', models.CharField(max_length=30)),
                ('leader_ship_agent_details', models.CharField(max_length=300)),
            ],
        ),
    ]
