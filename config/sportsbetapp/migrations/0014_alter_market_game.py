# Generated by Django 4.1.7 on 2023-06-01 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportsbetapp', '0013_alter_market_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='market', to='sportsbetapp.game'),
        ),
    ]