from re import template
from django.views.generic import TemplateView, FormView
from . import api_services
from .forms import CreateUserForm
from django.http import HttpResponseRedirect

"""
Class based view for the main page showing character page 1
"""
class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "pk" not in kwargs:
            kwargs['pk'] = 1
        information = api_services.get_all_characters(kwargs['pk'])
        character_lst = information['character_lst']
        num_pages = information['num_pages']
        context['information'] = {
            'page_id': kwargs['pk'],
            'characters' : character_lst,
            'pages': range(1, num_pages + 1)
        }
        return context

"""
Class based view showing a detailed character page

args: <int: pk> : character id
"""
class CharacterDetail(TemplateView):
    template_name = 'character_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        character_detail = api_services.get_character_detail(kwargs['pk'])
        context['information'] = character_detail
        return context
    
"""
Class based view showing the list of episodes
"""
class EpisodeIndex(TemplateView):
    template_name = 'episode_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        episode_detail = api_services.get_all_episodes()
        context['information'] = episode_detail
        return context
    
"""
Class based view showing a detailed episode
 
args: <int: pk> : episode id
"""
class EpisodeDetail(TemplateView):
    template_name = 'episode_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
"""
Class based Form view that will render a User registration form
"""
class CreateUserView(FormView):
    template_name = 'register.html'
    form_class = CreateUserForm
    success_url = "register_success"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

"""
Class based view that display successful registration
"""
class RegisterSuccessView(TemplateView):
    template_name = 'register_success.html'

    
    
        

