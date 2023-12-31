# Generated by Django 3.2.13 on 2023-09-04 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('stepNum', models.IntegerField()),
                ('utensils', models.CharField(max_length=20)),
                ('ingredients', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('tipType', models.CharField(max_length=25)),
                ('importance', models.CharField(choices=[('I', 'Important'), ('R', 'Relevant'), ('U', 'Unimportant')], max_length=1)),
                ('warning', models.CharField(max_length=100)),
            ],
        ),
    ]
