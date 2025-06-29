# Generated by Django 5.1.7 on 2025-04-04 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alignskills', '0003_basicinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('active', 'Active'), ('graduate', 'Graduate')], default='active', max_length=10)),
                ('certified', models.BooleanField(default=False)),
                ('certification_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
