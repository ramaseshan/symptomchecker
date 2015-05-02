from django.views import generic
from django.shortcuts import render
import better

def HomePage(request):
    if request.method == "POST":
        print request.POST
        symps = better.parse_record(str(request.POST.get("symptoms")))
        print symps  
        return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})


class AboutPage(generic.TemplateView):
    template_name = "about.html"

