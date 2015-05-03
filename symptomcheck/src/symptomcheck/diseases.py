from .models import Symptoms, Disease

#This is a probability algorithm applied on the database, which decremenntally gets diseases that match the given symptom.
# If sym1, sym2 and sym3 are the input, it will fetch the diseases matching all 3, and diseases matching any 2 and diseases matching any 1. That pretty much is a complex query that makes iterative database queries making a better probability algorithm.
# This function returns a list of dicts.

# This is incomplete

def sublists(symps):
    # sample input [1,2,3] Ex Output [[1],[2],[3],[1,2],[2,3],[1,3],[1,2,3]] 
    length = len(symps)
    i = 0
    poss = []
    while i < length:
        size = length - i
        print [sublist for sublist in (symps[x:x+size] for x in range(len(symps) - size + 1))]
        i = i +1
    return poss

def get_diseases(symps,possibilities):
    proab_diseases = []
    #ordered_disease = []
    # Get all the diseases that has atlease one of the symptoms.
    proab_diseases = Disease.objects.filter(d_symp__in=symps).distinct()
    return proab_diseases
