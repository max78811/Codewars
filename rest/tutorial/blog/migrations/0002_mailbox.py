# Generated by Django 3.2.7 on 2021-09-16 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=50)),
                ('mailbox', models.EmailField(max_length=254)),
            ],
        ),
    ]
