from django.db import models

class Symptoms(models.Model):
    symid = models.AutoField(primary_key=True)
    sym_name = models.CharField(max_length=100,blank=False,null=False)
    
    def __unicode__(self):
        return self.sym_name

class Disease(models.Model):
    did = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=100,blank=False,null=False)
    d_desc = models.TextField()
    d_symp = models.ManyToManyField(Symptoms)
    d_doctor1 = models.TextField()
    d_doctor2 = models.TextField(blank=True,null=True)
    d_doctor3 = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return self.d_name
