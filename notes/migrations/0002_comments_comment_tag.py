# Generated by Django 2.1 on 2018-11-18 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_tag',
            field=models.CharField(blank=True, choices=[('PYTHON', 'PYTHON'), ('DJANGO', 'DJANGO'), ('JAVA', 'JAVA'), ('MYSQL', 'MYSQL'), ('MACHINE_LEARNING', 'MACHINE_LEARNING'), ('JAVASCRIPT', 'JAVASCRIPT'), ('FRONT_END', 'FRONT_END'), ('C/C++', 'C/C++')], max_length=100),
        ),
    ]
