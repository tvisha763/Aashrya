# Generated by Django 4.0.6 on 2022-12-10 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='project.user'),
        ),
        migrations.AddField(
            model_name='shelter',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='shelters', to='project.user'),
        ),
    ]
