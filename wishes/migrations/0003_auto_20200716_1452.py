# Generated by Django 3.0.4 on 2020-07-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0002_auto_20200716_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='by',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='wish',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='wish',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
