# Generated by Django 2.2.4 on 2019-09-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0035_auto_20190910_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post_create',
            name='blog_post_image',
            field=models.ImageField(default=1, upload_to='photos/%Y/%m/%d/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='index_house_details',
            name='beds',
            field=models.IntegerField(max_length=2),
        ),
    ]
