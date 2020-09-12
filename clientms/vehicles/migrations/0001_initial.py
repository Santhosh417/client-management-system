# Generated by Django 2.2.16 on 2020-09-11 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(default='2000', max_length=4)),
                ('make', models.CharField(default=' ', max_length=50)),
                ('model', models.CharField(blank=True, default=' ', max_length=50, null=True)),
                ('vin_number', models.CharField(default=' ', max_length=50)),
                ('date_of_purchase', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]