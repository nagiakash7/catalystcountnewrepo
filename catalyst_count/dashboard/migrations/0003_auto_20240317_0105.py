# Generated by Django 3.2.1 on 2024-03-16 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_uploadedcsv_year_founded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedcsv',
            name='current_employee_estimate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='uploadedcsv',
            name='total_employee_estimate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
