# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Site, Measurement

class ManageSites(admin.ModelAdmin):
  model=Site
  list_display=('name','id')

class ManageMeasurements(admin.ModelAdmin):
  model=Measurement
  list_display=('site','date','a','b')
  
admin.site.register(Site, ManageSites)
admin.site.register(Measurement, ManageMeasurements)
