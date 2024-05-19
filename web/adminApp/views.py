from django.shortcuts import render,get_object_or_404,redirect
from SchoolApp.forms import CourForm, MatiereForm
from django.http import HttpResponseRedirect,HttpResponse
from adminApp.models import Cour, Matiere
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.urls import reverse

# Create your views here.

@login_required

class MatiereIndexView(ListView):
    model=Matiere
    template_name="adminApp/index.html"
    context_object_name="matieres"

def home(request):
    context={
        'matieres':Matiere.objects.all()
    }
    return render(request,'adminApp/index.html',context=context)

def root(request):
    context={
        'matieres':Matiere.objects.all()
    }
    return redirect('user/',context=context)


class CoursCreateView(CreateView):
    model=Cour
    template_name="adminApp/new.html"
    form_class=CourForm


@login_required   
def newCours(request,matiere=""):
    context={}
    ok=-1
    if matiere:
        context['matiere']=get_object_or_404(Matiere,slug=matiere)
    if request.method=="POST":
        form=CourForm(request.POST,request.FILES)
        if request.FILES:
            type_f=(request.FILES)['file'].content_type
            if not (type_f in ['text/plain','application/pdf','video/mp4','video/mpeg','video/avi']):
                ok=0
            elif form.is_valid():
                form.cleaned_data
                c=form.save(commit=False)
                if Cour.objects.filter(slug=c.getSlug,matiere=c.matiere):
                    ok=0
                elif c.checked():
                    c.save()
                    ok=1
                    form=CourForm(initial=context)
                else:
                    ok=0  
            else:
                ok=0
    else:
        form=CourForm(initial=context)
    return render(request,'adminApp/new.html',context={'form':form,'ok':ok,'title':'Enregister un nouveau cours'})
class MatiereCreateView(CreateView):
    model=Matiere
    template_name="adminApp/new.html"
    form_class=MatiereForm
@login_required
def newMatiere(request):
    ok=-1
    if request.method=="POST":
        form=MatiereForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            mat=form.save(commit=False)
            test=Matiere.objects.filter(title=mat.title)
            slug=Matiere.objects.filter(slug=mat.getSlug)
            if any([test,slug]):
                ok=0
            else:
                mat.save()
                ok=1
            form=MatiereForm()
        else:
            ok=0
    else:
        form=MatiereForm()
    return render(request,'adminApp/new.html',context={'form':form,'ok':ok,'title':'Enregistrer une Nouvelle matiere'})