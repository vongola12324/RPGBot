from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100, default="Player")


class PetSkill(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    modHP = models.FloatField()
    modAtk = models.FloatField()
    modDef = models.FloatField()
    directAttack = models.IntegerField()
    directAttackPer = models.IntegerField()

    def __unicode__(self):
        return self.name


class PetStatus(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    noAtk = models.PositiveIntegerField(default=0)
    allyAtkPer = models.PositiveIntegerField(default=0)
    selfAtkPer = models.PositiveIntegerField(default=0)
    modAtk = models.IntegerField()
    modDef = models.IntegerField()


class PetPrototype(models.Model):
    name = models.CharField(max_length=100)
    story = models.TextField()
    maxHP = models.IntegerField()
    maxAtk = models.IntegerField()
    maxDef = models.IntegerField()
    minHP = models.IntegerField()
    minAtk = models.IntegerField()
    minDef = models.IntegerField()
    skills = models.ManyToManyField(PetSkill, blank=True)
    maxLevel = models.PositiveIntegerField()


class Pet(models.Model):
    player = models.ForeignKey(Profile)
    proto = models.ForeignKey(PetPrototype)
    level = models.PositiveIntegerField()
    status = models.ManyToManyField(PetStatus)

# class PetEvolution(models.Model):
#     frm = models.ForeignKey(PetPrototype)
#     dst = models.OneToOneField(PetPrototype)
