from turtle import title
from django.shortcuts import render,get_object_or_404

from adminApp.models import Matiere,Cour

# Create your views here.

matieres=Matiere.objects.all()
def home(request):
    cours=Cour.objects.order_by('-view')[:8]
    return render(request,'userApp/index.html',context={'Vue':"Most View courses",'matieres':matieres,'cours':cours})

def matiere(request,matiere):
    mat=get_object_or_404(Matiere,slug=matiere)
    return render(request,'userApp/index.html',context={'Vue':mat.title,'cours':mat.cour_set.all,'matieres':matieres})

def cours(request,matiere,cours):
    mat=get_object_or_404(Matiere,slug=matiere)
    cour=get_object_or_404(Cour,matiere=mat,slug=cours)
    cour.view+=1
    cour.save()
    return render(request,'userApp/show.html',context={'cour':cour})
