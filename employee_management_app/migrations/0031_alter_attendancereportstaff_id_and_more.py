# Generated by Django 4.0.6 on 2022-12-25 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_app', '0030_merge_20221225_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancereportstaff',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='PayrollReportStaff',
        ),
    ]
