import re
import sys
sex_pat=re.compile(r'\b(he|she|I)\b',re.IGNORECASE)
unwanted_pat = re.compile(r'\b(have|having|suffering|feeling|am|is|from|and)\b',re.IGNORECASE)
symptom_pat=re.compile(r'[,-]')

def parse_record(astr):
    print astr
    match=unwanted_pat.search(astr)    
    if match:
        astr=unwanted_pat.sub('',astr)
    else: print('No unwanted string found')
    match=sex_pat.search(astr)    
    if match:
        sex=match.group(1)
        sex='Female' if sex.lower().startswith('s') else 'Male'
        astr,_=sex_pat.subn('',astr,1)
    else: print('Can not find sex.Does it matter ?')

    astr=astr.replace('and',' ')    
    symptoms=[s.strip() for s in symptom_pat.split(astr)]
    for s in symptoms:
		print "Symptoms are " + ",".join(s.split())
    return {
            'Symptoms': symptoms,
            }

"""
Sample answer :
I am suffering from cold and cough
Symptoms are cold,cough
I am having flu
Symptoms are flu


"""

if __name__=='__main__':
    tests=('I am suffering from cold and cough','I am having flu')

    for record in tests:
        result=parse_record(record)
