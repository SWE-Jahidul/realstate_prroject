# Generated by Django 2.2.4 on 2019-09-02 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_index_house_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='index_defoult_change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('why_choose', models.CharField(default='', max_length=50)),
                ('chose_details', models.CharField(default='', max_length=50)),
                ('recent_blog_hedings', models.CharField(default='', max_length=50)),
                ('recent_blog_details', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
