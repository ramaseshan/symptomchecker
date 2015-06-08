from .models import Symptoms

# Auto check if the symptom exists , else create it
def check_and_add_sym(symps):
    act_symps = []
    for s in symps:
       obj, created = Symptoms.objects.get_or_create(sym_name__iexact=s) 
       act_symps.append(obj)
    return act_symps

