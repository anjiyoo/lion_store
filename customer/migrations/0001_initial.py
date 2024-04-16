# Generated by Django 5.0.4 on 2024-04-16 02:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.food')),
            ],
        ),
    ]
