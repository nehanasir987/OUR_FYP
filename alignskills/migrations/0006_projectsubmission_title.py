# Generated by Django 5.1.7 on 2025-04-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alignskills', '0005_customuser_address_customuser_education_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsubmission',
            name='title',
            field=models.CharField(blank=True, default='untitle projects', max_length=100, null=True),
        ),
    ]
