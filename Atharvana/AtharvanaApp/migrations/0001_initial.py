# Generated by Django 4.0.3 on 2022-03-02 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mm', models.CharField(blank=True, max_length=50, null=True)),
                ('s1', models.CharField(blank=True, max_length=50, null=True)),
                ('s2', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created')),
            ],
        ),
    ]
