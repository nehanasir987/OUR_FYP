# Generated by Django 5.1.7 on 2025-04-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alignskills', '0012_alter_comment_options_rename_user_id_comment_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsubmission',
            name='category',
            field=models.CharField(choices=[('AI', 'Artificial Intelligence'), ('IT', 'Information Technology'), ('DB', 'Database'), ('js', 'javascript'), ('py', 'python'), ('ccn', 'computer network')], default='AI', max_length=10),
        ),
    ]
