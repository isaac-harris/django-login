# Generated by Django 2.1.2 on 2020-05-28 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=64)),
                ('customerDOB', models.DateField(max_length=8)),
                ('customerPhone', models.CharField(max_length=64)),
                ('customerEmail', models.CharField(max_length=64)),
                ('customerAddress', models.CharField(max_length=64)),
            ],
        ),
    ]