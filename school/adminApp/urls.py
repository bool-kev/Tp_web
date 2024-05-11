from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='admin.home'),
    path('new_cours/',newCours,name='new.cours'),
    path('new_cours/<slug:matiere>',newCours,name='new.cours.matiere'),
    path('new_matiere/',newMatiere,name='new.matiere'),
]
