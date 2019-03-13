from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    Name = models.CharField(max_length=200)
    Race = models.CharField(max_length=200, default ='Human')
    level = models.IntegerField(default =1)
    Bard = 'Bd'
    Barbarian = 'Bb'
    Cleric = 'Cl'
    Druid = 'Dr'
    Fighter = 'Fg'
    Monk = 'Mk'
    Paladin = 'Pd'
    Rogue = 'Rg'
    Ranger = 'Rn'
    Sorcerer = 'Sr'
    Wizard = 'Wz'
    Warlock = 'Wk'
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
    Class = models.CharField(max_length=2,
        choices = Class,
        default = Bard)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title