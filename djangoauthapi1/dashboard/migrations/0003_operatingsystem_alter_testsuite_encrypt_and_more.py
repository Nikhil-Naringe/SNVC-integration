# Generated by Django 4.0.3 on 2024-02-01 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_testsuite_host_ip_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('centos', 'CentOS'), ('windows', 'Windows'), ('ubuntu', 'Ubuntu')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='testsuite',
            name='encrypt',
            field=models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], default=False),
        ),
        migrations.AlterField(
            model_name='testsuite',
            name='protocol',
            field=models.CharField(choices=[('SMB', 'SMB'), ('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3'), ('P4', 'P4')], max_length=50),
        ),
        migrations.AlterField(
            model_name='testsuite',
            name='sign',
            field=models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], default=True),
        ),
        migrations.AlterField(
            model_name='testsuite',
            name='trace',
            field=models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], default=False),
        ),
        migrations.CreateModel(
            name='TestSuiteName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(help_text='Enter folder location', max_length=200)),
                ('operating_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.operatingsystem')),
                ('test_suite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.testsuite')),
            ],
        ),
    ]