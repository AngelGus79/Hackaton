from __future__ import unicode_literals

from django.db import models

# Create your models here.


class modelLey(models.Model):
    Ag = models.FloatField()
    Av = models.FloatField()
    Pd = models.FloatField()
    Zn = models.FloatField()
    Cu = models.FloatField()
