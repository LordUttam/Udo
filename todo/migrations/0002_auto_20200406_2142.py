# Generated by Django 3.0.4 on 2020-04-06 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
