# Generated by Django 4.0.4 on 2022-05-12 14:28

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('routing', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elevated_geometry', django.contrib.gis.db.models.fields.LineStringField(dim=3, srid=4326)),
                ('sg', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='routing.sg')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('geometry', django.contrib.gis.db.models.fields.LineStringField(geography=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Waypoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.IntegerField()),
                ('elevated_geometry', django.contrib.gis.db.models.fields.PointField(dim=3, srid=4326)),
                ('connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waypoints', to='composer.connection')),
            ],
        ),
        migrations.CreateModel(
            name='RouteSGBinding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed', models.BooleanField(default=False)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bound_sgs', to='composer.route')),
                ('sg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bound_routes', to='routing.sg')),
            ],
        ),
    ]