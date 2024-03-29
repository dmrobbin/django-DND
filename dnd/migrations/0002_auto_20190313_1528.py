# Generated by Django 2.1.7 on 2019-03-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='Name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='Class',
            field=models.CharField(choices=[('Bd', 'Bard'), ('Bb', 'Barbarian'), ('Cl', 'Cleric'), ('Dr', 'Druid'), ('Fg', 'Fighter'), ('Mk', 'Monk'), ('Pd', 'Paladin'), ('Rg', 'Rogue'), ('Rn', 'Ranger'), ('Sr', 'Sorcerer'), ('Wk', 'Warlock'), ('Wz', 'Wizard')], default='Bd', max_length=2),
        ),
        migrations.AddField(
            model_name='post',
            name='Race',
            field=models.CharField(default='Human', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
