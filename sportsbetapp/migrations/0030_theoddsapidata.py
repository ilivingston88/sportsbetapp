# Generated by Django 4.1.7 on 2023-08-15 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsbetapp', '0029_bookmaker_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheOddsAPIData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
