# Generated by Django 5.0.6 on 2024-07-12 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_uploadedfile_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('y_email', models.EmailField(max_length=250)),
                ('y_subject', models.CharField(max_length=200)),
                ('y_message', models.CharField(max_length=500)),
            ],
        ),
    ]
