# Generated by Django 3.0.1 on 2020-06-05 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('submitter', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('breed', models.CharField(blank=True, max_length=30)),
                ('description', models.TextField()),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('submittion_date', models.DateTimeField()),
                ('age', models.IntegerField(null=True)),
                ('vacccinationn', models.ManyToManyField(blank=True, to='adoptions.Vaccine')),
            ],
        ),
    ]
