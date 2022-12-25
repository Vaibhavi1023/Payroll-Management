# Generated by Django 4.1.3 on 2022-12-20 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_app', '0025_staffs2_delete_staffs1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staffs3',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.group')),
                ('site_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.site')),
            ],
        ),
        migrations.DeleteModel(
            name='Staffs2',
        ),
    ]