# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Site(models.Model):
  name=models.CharField(max_length=100)

class Measurement(models.Model):
  date=models.DateField()
  a=models.DecimalField(max_digits=6, decimal_places=2)
  b=models.DecimalField(max_digits=6, decimal_places=2)
  site=models.ForeignKey(Site,on_delete=models.CASCADE)