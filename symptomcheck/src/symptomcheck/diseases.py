from .models import Symptoms, Disease
from django.db.models import Q

#This is a probability algorithm applied on the database, which decremenntally gets diseases that match the given symptom.
# If sym1, sym2 and sym3 are the input, it will fetch the diseases matching all 3, and diseases matching any 2 and diseases matching any 1. That pretty much is a complex query that makes iterative database queries making a better probability algorithm.
# This function returns a list of dicts.

# This is incomplete

def sublists(symps):
    import itertools
    combs = []

    for i in xrange(1, len(symps)+1):
        els = [list(x) for x in itertools.combinations(symps, i)]
        combs.extend(els)
    return combs

def get_diseases(symps,possibilities):
    proab_diseases = []
    # Get all the diseases that has atlease one of the symptoms.
    proab_diseases1 = Disease.objects.filter(d_symp__in=symps).distinct()
    return proab_diseases1
