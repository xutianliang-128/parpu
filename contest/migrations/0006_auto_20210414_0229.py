# Generated by Django 3.1.7 on 2021-04-13 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0005_auto_20210413_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='area',
            field=models.CharField(choices=[('Business', 'business'), ('Investment', 'investment'), ('Technology', 'technology'), ('Hackson', 'hackson'), ('Mathematics', 'mathematics'), ('Sports', 'sports'), ('Debate', 'debate'), ('Cooking', 'cooking')], default='B', max_length=80),
        ),
    ]
