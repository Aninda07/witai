# Generated by Django 3.2 on 2022-09-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0017_auto_20220914_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Utterance_Changed',
            new_name='Details',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Utterance_End',
            new_name='Entities',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Utterance_Body',
            new_name='Shrug',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Utterance_Start',
            new_name='Traits',
        ),
        migrations.RenameField(
            model_name='montact',
            old_name='Or_Use_New_Intent',
            new_name='Chat',
        ),
        migrations.RenameField(
            model_name='montact',
            old_name='Old_Utterance',
            new_name='Intent',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='Delete_Entity',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='Utterance_Entities',
        ),
        migrations.RemoveField(
            model_name='montact',
            name='Delete_Intent',
        ),
        migrations.RemoveField(
            model_name='montact',
            name='Traits',
        ),
        migrations.RemoveField(
            model_name='montact',
            name='Use_Built_In_Intent',
        ),
        migrations.AddField(
            model_name='montact',
            name='Sender_ID',
            field=models.CharField(default='10000', max_length=200),
        ),
    ]
