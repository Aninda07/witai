# Generated by Django 3.2 on 2022-09-01 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_rename_text_contact_utterance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='response',
            new_name='Utterance_Changed',
        ),
        migrations.AddField(
            model_name='contact',
            name='New_Intent',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Body',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='End',
            field=models.CharField(default='null', max_length=500),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Entities',
            field=models.CharField(default='null', max_length=500),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Intent',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Start',
            field=models.CharField(default='null', max_length=500),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Traits',
            field=models.CharField(default='null', max_length=500),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Utterance',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
