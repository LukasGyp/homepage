# Generated by Django 3.2.5 on 2022-06-03 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blogpost_blogtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created',
            field=models.DateField(help_text='作成日'),
        ),
    ]