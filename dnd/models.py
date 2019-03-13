from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    Name = models.CharField(max_length=200)
    Race = models.CharField(max_length=200, default ='Human')
    Level = models.IntegerField(default =1)
    Bard = 'Bard'
    Barbarian = 'Barbarian'
    Cleric = 'Cleric'
    Druid = 'Druid'
    Fighter = 'Figher'
    Monk = 'Monk'
    Paladin = 'Paladin'
    Rogue = 'Rogue'
    Ranger = 'Ranger'
    Sorcerer = 'Sorcerer'
    Wizard = 'Wizard'
    Warlock = 'Warlock'
    Class = (
        (Bard, 'Bard'),
        (Barbarian, 'Barbarian'),
        (Cleric, 'Cleric'),
        (Druid, 'Druid'),
        (Fighter, 'Fighter'),
        (Monk, 'Monk'),
        (Paladin, 'Paladin'),
        (Rogue, 'Rogue'),
        (Ranger, 'Ranger'),
        (Sorcerer, 'Sorcerer'),
        (Warlock, 'Warlock'),
        (Wizard, 'Wizard'),
    )
    Class = models.CharField(max_length=12,
        choices = Class,
        default = Bard)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Name