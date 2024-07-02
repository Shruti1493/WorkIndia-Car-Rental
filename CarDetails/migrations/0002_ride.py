# Generated by Django 4.2.6 on 2024-07-02 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CarDetails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('hours_requirement', models.IntegerField()),
                ('amount', models.FloatField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDetails.car')),
            ],
        ),
    ]
