# Generated by Django 2.2 on 2020-06-24 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_auto_20200624_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phoneNumber',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
