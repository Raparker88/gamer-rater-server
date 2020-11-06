# Generated by Django 3.1.3 on 2020-11-06 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raterapi', '0002_remove_playergame_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=1000)),
                ('playergame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.playergame')),
            ],
        ),
    ]
