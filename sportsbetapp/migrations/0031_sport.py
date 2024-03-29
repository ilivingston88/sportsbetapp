# Generated by Django 4.1.7 on 2023-08-16 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsbetapp', '0030_theoddsapidata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('key', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
