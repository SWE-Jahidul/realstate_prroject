# Generated by Django 2.2.4 on 2019-09-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contract_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='details',
        ),
    ]