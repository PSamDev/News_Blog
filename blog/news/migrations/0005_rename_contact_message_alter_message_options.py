# Generated by Django 4.1.5 on 2023-03-28 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Message',
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
    ]
