# Generated by Django 5.0.4 on 2024-05-14 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('permission1', 'Can perform tasks requiring permission1'), ('permission2', 'Can perform tasks requiring permission2'), ('permission3', 'Can perform tasks requiring permission3')),
            },
        ),
    ]