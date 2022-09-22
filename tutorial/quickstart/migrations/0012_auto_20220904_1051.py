# Generated by Django 3.2 on 2022-09-04 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0011_alter_contact_intent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='New_Intent',
            new_name='Or_Use_New_Intent',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='Intent',
        ),
        migrations.AddField(
            model_name='contact',
            name='Use_Built_In_Intent',
            field=models.CharField(choices=[('buy_flowers', 'buy_flowers'), ('Flight_Book', 'Flight_Book'), ('Hotel_Book', 'Hotel_Book'), ('tourist_place', 'tourist_place'), ('wit/add_time_timer', 'wit/add_time_timer'), ('wit/add_to_playlist', 'wit/add_to_playlist'), ('wit/cancel', 'wit/cancel'), ('wit/check_weather_condition', 'wit/check_weather_condition'), ('wit/confirmation', 'wit/confirmation'), ('wit/create_alarm', 'wit/create_alarm'), ('wit/create_playlist', 'wit/create_playlist'), ('wit/create_timer', 'wit/create_timer'), ('wit/decrease_volume', 'wit/decrease_volume'), ('wit/delete_alarm', 'wit/delete_alarm'), ('wit/delete_playlist', 'wit/delete_playlist'), ('wit/delete_timer', 'wit/delete_timer'), ('wit/dislike_music', 'wit/dislike_music'), ('wit/fast_forward_track', 'wit/fast_forward_track'), ('wit/get_alarms', 'wit/get_alarms'), ('wit/get_date', 'wit/get_date'), ('wit/get_date', 'wit/get_date'), ('wit/get_sunset', 'wit/get_sunset'), ('wit/get_temperature', 'wit/get_temperature'), ('wit/get_timer', 'wit/get_timer'), ('wit/get_track_info', 'wit/get_track_info'), ('wit/get_weather', 'wit/get_weather'), ('wit/go_back', 'wit/go_back'), ('wit/go_forward', 'wit/go_forward'), ('wit/increase_volume', 'wit/increase_volume'), ('wit/like_music', 'wit/like_music'), ('wit/loop_music', 'wit/loop_music'), ('wit/negation', 'wit/negation'), ('wit/nevermind', 'wit/nevermind'), ('wit/open_resource', 'wit/open_resource'), ('wit/pause', 'wit/pause'), ('wit/pause_music', 'wit/pause_music'), ('wit/pause_timer', 'wit/pause_timer'), ('wit/play', 'wit/play'), ('wit/play_music', 'wit/play_music'), ('wit/play_podcast', 'wit/play_podcast'), ('wit/previous_track', 'wit/previous_track'), ('wit/remove_from_playlist', 'wit/remove_from_playlist'), ('wit/repeat_response', 'wit/repeat_response'), ('wit/replay_track', 'wit/replay_track'), ('wit/resume_timer', 'wit/resume_timer'), ('wit/rewind_track', 'wit/rewind_track'), ('wit/select_item', 'wit/select_item'), ('wit/share', 'wit/share'), ('wit/shuffle_playlist', 'wit/shuffle_playlist'), ('wit/silence_alarm', 'wit/silence_alarm'), ('wit/skip_track', 'wit/skip_track'), ('wit/snooze_alarm', 'wit/skip_track'), ('wit/stop', 'wit/stop'), ('wit/stop_music', 'wit/stop_music'), ('wit/subtract_time_timer', 'wit/subtract_time_timer'), ('wit/unloop_music', 'wit/unloop_music'), ('wit/unshuffle_playlist', 'wit/unshuffle_playlist')], default='null', max_length=200),
        ),
    ]
