# Generated by Django 4.1.4 on 2022-12-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_input_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
