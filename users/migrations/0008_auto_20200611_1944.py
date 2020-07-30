# Generated by Django 3.0.6 on 2020-06-11 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200514_0509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='provinsi_selain_indo',
            new_name='provinsi_selain_indonesia',
        ),
        migrations.AlterField(
            model_name='profile',
            name='negara',
            field=models.CharField(choices=[('Indonesia', 'Indonesia'), ('Luar Negeri', 'Luar Negeri')], max_length=30, null=True),
        ),
    ]