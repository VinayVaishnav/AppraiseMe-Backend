# Generated by Django 4.2.1 on 2023-10-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_profiles_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='work_exp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=40)),
                ('title', models.CharField(max_length=20)),
                ('emp_type', models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time')], max_length=10)),
                ('company', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('location_type', models.CharField(choices=[('Onsite', 'Onsite'), ('Hybrid', 'Hybrid'), ('Remote', 'Remote')], max_length=30)),
                ('currently_working', models.BooleanField()),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
            ],
        ),
    ]
