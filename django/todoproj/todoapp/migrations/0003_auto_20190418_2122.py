# Generated by Django 2.2 on 2019-04-18 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20190418_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='todoapp.TodoList'),
            preserve_default=False,
        ),
    ]
