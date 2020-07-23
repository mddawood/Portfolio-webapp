from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import About, Education, Experience, Tool

# Create your views here.
# def index(request):
#     about = About.objects.all()
#     return render(request, 'home.html', {'about': about})

# class About(ListView):
#     model = About
#     context_object_name = 'abouts'
#     template_name = 'index.html'

class About(ListView):
    context_object_name = 'abouts'
    template_name = 'index.html'
    queryset = About.objects.all()

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['experiences'] = Experience.objects.all()
        context['educations'] = Education.objects.all()
        context['tools'] = Tool.objects.all()
        # And so on for more models
        return context
