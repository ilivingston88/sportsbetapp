# Generated by Django 4.1.7 on 2023-06-02 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsbetapp', '0022_rename_gameoutcome_outcome_remove_game_bookmakers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outcome',
            name='bookmaker',
        ),
        migrations.RemoveField(
            model_name='outcome',
            name='game',
        ),
        migrations.DeleteModel(
            name='Bookmaker',
        ),
        migrations.DeleteModel(
            name='Outcome',
        ),
    ]
