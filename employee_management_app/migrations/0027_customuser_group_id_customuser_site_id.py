# Generated by Django 4.1.3 on 2022-12-20 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_app', '0026_staffs3_delete_staffs2'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='group_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.group'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='site_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.site'),
        ),
    ]
