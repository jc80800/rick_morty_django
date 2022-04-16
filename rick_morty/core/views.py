from re import template
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

class CharacterDetail(TemplateView):
    template_name = 'character_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        character_detail = api_services.get_character_detail(kwargs['pk'])
        context['information'] = character_detail
        return context
    
class EpisodeIndex(TemplateView):
    template_name = 'episode_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        episode_detail = api_services.get_all_episodes()
        context['information'] = episode_detail
        return context
    
        

