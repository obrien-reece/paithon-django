# Generated by Django 4.2.5 on 2023-10-03 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminder_txt', models.CharField(max_length=200)),
                ('reminder_date', models.DateTimeField(verbose_name='reminder_date')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.day')),
            ],
        ),
    ]