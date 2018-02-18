# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView
from .models import Site, Measurement
from django.db.models import Sum

class SiteList(ListView):
    template_name = 'site_list.html'
    model = Site

class SiteDetails(TemplateView):
    template_name = 'measurement_list.html'
    def get_context_data(self, **kwargs):
        context = super(SiteDetails, self).get_context_data(**kwargs)
        self.site = get_object_or_404(Site, id=self.kwargs['site'])
        context['measurement_list'] = Measurement.objects.filter(site=self.site)
        context['site'] = self.site
        return context

class SummarySum(TemplateView):
    template_name = 'summary.html'    
    def get_context_data(self, **kwargs):
        context = super(SummarySum, self).get_context_data(**kwargs)        
        context['sum_list'] = Site.objects.annotate(value_a=Sum('measurement__a'),value_b=Sum('measurement__b'))
        return context

class SummaryAverage(TemplateView):
    template_name = 'summary.html'    
    def get_context_data(self, **kwargs):
        context = super(SummaryAverage, self).get_context_data(**kwargs)        
        context['sum_list'] = Site.objects.raw("SELECT s.id, s.name, round(avg(m.a),2) AS value_a, round(avg(m.b),2) AS value_b FROM solar_calc_site s LEFT JOIN solar_calc_measurement m ON s.id=m.site_id GROUP BY s.id, s.name")
        return context
