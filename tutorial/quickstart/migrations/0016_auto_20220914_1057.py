# Generated by Django 3.2 on 2022-09-14 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0015_auto_20220905_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='Delete_Intent',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='Or_Use_New_Intent',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='Traits',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='Use_Built_In_Intent',
        ),
        migrations.CreateModel(
            name='Montact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Traits', models.CharField(default='null', max_length=500)),
                ('Or_Use_New_Intent', models.CharField(default='null', max_length=200)),
                ('Use_Built_In_Intent', models.CharField(choices=[('new_car', 'new_car'), ('Room_Book', 'Room_Book'), ('tourist_place', 'tourist_place'), ('null', 'null'), ('tourist_place', 'tourist_place'), ('wit$pause_music', 'wit$pause_music'), ('buy_flowers', 'buy_flowers'), ('Flight_Book', 'Flight_Book'), ('Hotel_Book', 'Hotel_Book'), ('tourist_place', 'tourist_place'), ('wit/add_time_timer', 'wit/add_time_timer'), ('wit/add_to_playlist', 'wit/add_to_playlist'), ('wit/cancel', 'wit/cancel'), ('wit/check_weather_condition', 'wit/check_weather_condition'), ('wit/confirmation', 'wit/confirmation'), ('wit/create_alarm', 'wit/create_alarm'), ('wit/create_playlist', 'wit/create_playlist'), ('wit/create_timer', 'wit/create_timer'), ('wit/decrease_volume', 'wit/decrease_volume'), ('wit/delete_alarm', 'wit/delete_alarm'), ('wit/delete_playlist', 'wit/delete_playlist'), ('wit/delete_timer', 'wit/delete_timer'), ('wit/dislike_music', 'wit/dislike_music'), ('wit/fast_forward_track', 'wit/fast_forward_track'), ('wit/get_alarms', 'wit/get_alarms'), ('wit/get_date', 'wit/get_date'), ('wit/get_date', 'wit/get_date'), ('wit/get_sunset', 'wit/get_sunset'), ('wit/get_temperature', 'wit/get_temperature'), ('wit/get_timer', 'wit/get_timer'), ('wit/get_track_info', 'wit/get_track_info'), ('wit/get_weather', 'wit/get_weather'), ('wit/go_back', 'wit/go_back'), ('wit/go_forward', 'wit/go_forward'), ('wit/increase_volume', 'wit/increase_volume'), ('wit/like_music', 'wit/like_music'), ('wit/loop_music', 'wit/loop_music'), ('wit/negation', 'wit/negation'), ('wit/nevermind', 'wit/nevermind'), ('wit/open_resource', 'wit/open_resource'), ('wit/pause', 'wit/pause'), ('wit/pause_music', 'wit/pause_music'), ('wit/pause_timer', 'wit/pause_timer'), ('wit/play', 'wit/play'), ('wit/play_music', 'wit/play_music'), ('wit/play_podcast', 'wit/play_podcast'), ('wit/previous_track', 'wit/previous_track'), ('wit/remove_from_playlist', 'wit/remove_from_playlist'), ('wit/repeat_response', 'wit/repeat_response'), ('wit/replay_track', 'wit/replay_track'), ('wit/resume_timer', 'wit/resume_timer'), ('wit/rewind_track', 'wit/rewind_track'), ('wit/select_item', 'wit/select_item'), ('wit/share', 'wit/share'), ('wit/shuffle_playlist', 'wit/shuffle_playlist'), ('wit/silence_alarm', 'wit/silence_alarm'), ('wit/skip_track', 'wit/skip_track'), ('wit/snooze_alarm', 'wit/skip_track'), ('wit/stop', 'wit/stop'), ('wit/stop_music', 'wit/stop_music'), ('wit/subtract_time_timer', 'wit/subtract_time_timer'), ('wit/unloop_music', 'wit/unloop_music'), ('wit/unshuffle_playlist', 'wit/unshuffle_playlist')], default='null', max_length=200)),
                ('Delete_Intent', models.CharField(default='0', max_length=200)),
                ('Old_Intents', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quickstart.contact')),
            ],
        ),
    ]