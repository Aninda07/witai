# Generated by Django 3.2 on 2022-09-03 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0007_remove_contact_utterance_entities'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Utterance_Entities',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
