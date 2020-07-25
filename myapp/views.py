from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import About, Education, Experience, Tool, Skill, Interest, Award

# using the below mentioned class based view we're passing the models to one single template 'index.html'
class About(ListView):
    context_object_name = 'abouts'
    template_name = 'index.html'
    queryset = About.objects.all()

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['experiences'] = Experience.objects.all()
        context['educations'] = Education.objects.all()
        context['tools'] = Tool.objects.all()
        context['skills'] = Skill.objects.all()
        context['interest'] = Interest.objects.all()
        context['awards'] = Award.objects.all()
        return context
