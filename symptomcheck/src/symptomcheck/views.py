from django.views import generic
from django.shortcuts import render
import better,check_sym, diseases
from .models import Symptoms, Disease

def HomePage(request):
    if request.method == "POST":
        symps = better.parse_record(str(request.POST.get("symptoms")))
        symps = check_sym.check_and_add_sym(symps)
        print diseases.get_diseases(symps)
        return render(request, 'home.html', {'symps':symps})
    else:
        return render(request, 'home.html', {})


class AboutPage(generic.TemplateView):
    template_name = "about.html"

