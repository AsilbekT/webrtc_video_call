# Generated by Django 3.2.5 on 2023-04-22 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_mobiletoken'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mobiletoken',
            options={'verbose_name': "Mobile user's token", 'verbose_name_plural': "Mobile users' token"},
        ),
    ]
