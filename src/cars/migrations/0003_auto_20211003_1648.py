# Generated by Django 3.2.7 on 2021-10-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20211003_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='last_revision',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='number_of_doors',
            field=models.IntegerField(default=4, verbose_name='No. of doors'),
        ),
    ]
