# Generated by Django 2.2.4 on 2019-09-10 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0034_index_house_details_house_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index_house_details',
            name='baths',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='index_house_details',
            name='beds',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='index_house_details',
            name='spaces',
            field=models.IntegerField(default=0),
        ),
    ]
