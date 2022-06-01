# Generated by Django 4.0.4 on 2022-05-31 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserPartner',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('userPartnerName', models.TextField(blank=True, default='')),
                ('userPartnerDate', models.IntegerField(blank=True, null=True)),
                ('userPartnerImage', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('preferenceEat', models.TextField(blank=True)),
                ('preferencePlay', models.TextField(blank=True)),
                ('preferenceDrink', models.TextField(blank=True)),
                ('preferenceSee', models.TextField(blank=True)),
                ('preferenceWalk', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('userName', models.TextField()),
                ('userEmail', models.TextField()),
                ('userId', models.TextField(primary_key=True, serialize=False)),
                ('userPassword', models.TextField()),
                ('userSex', models.TextField()),
                ('userAge', models.TextField()),
                ('userImage', models.TextField(blank=True, default='')),
                ('partner', models.OneToOneField(blank=True, db_column='partner', null=True, on_delete=django.db.models.deletion.CASCADE, to='User.userpartner')),
                ('preference', models.OneToOneField(blank=True, db_column='preference', null=True, on_delete=django.db.models.deletion.CASCADE, to='User.userpreference')),
            ],
        ),
    ]
