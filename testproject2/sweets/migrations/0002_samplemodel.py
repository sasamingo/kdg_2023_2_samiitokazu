# Generated by Django 4.2.7 on 2024-01-30 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
