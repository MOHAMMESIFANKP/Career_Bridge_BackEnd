# Generated by Django 4.2.4 on 2023-09-21 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_companyaddress_remove_companyinfo_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyinfo',
            name='address',
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='streetaddress',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='zipcode',
            field=models.BigIntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='CompanyAddress',
        ),
    ]
