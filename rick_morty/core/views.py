from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from . import api_services

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        character_lst = api_services.get_all_characters()
        context['information'] = {
            'characters' : character_lst
        }
        return context
