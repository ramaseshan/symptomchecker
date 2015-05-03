from django.views import generic
from django.shortcuts import render
import better,check_sym, diseases
from .models import Symptoms, Disease
from django.http import HttpResponse

def HomePage(request):
    if request.method == "POST":
        symps = better.parse_record(str(request.POST.get("symptoms")))
        symptoms = check_sym.check_and_add_sym(symps)
        possibilities = diseases.sublists(symptoms)
        disease_list = diseases.get_diseases(symptoms,possibilities)
        return render(request, 'home.html', {'symps':symps,'diseases':disease_list})
    else:
        return render(request, 'home.html', {})

def Learn(request):
    if request.is_ajax():
    #if request.method == dd
        id = request.POST.get('id')
        symps = request.POST.get('symptoms')
        disease = Disease.objects.get(did=id)
        for s in eval(symps):
            for d in disease.d_symp.all():
                if s == d:
                   pass
                else:
                    print "Comes here"
                    try:
                        sym = Symptoms.objects.get(sym_name=s)
                        print sym
                        disease.d_symp.add(sym)
                        disease.save()       
                        print disease        
                    except Exception as e:
                        print e
        return HttpResponse("Success") 

class AboutPage(generic.TemplateView):
    template_name = "about.html"

