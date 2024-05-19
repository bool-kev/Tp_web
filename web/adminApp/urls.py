from django.urls import path
from .views import *
app_name="adminApp"
urlpatterns = [
    path('',home,name='home'),
    path('new_cours/',CoursCreateView.as_view(),name='new.cours'),
    path('new_cours/<slug:matiere>',newCours,name='new.cours.matiere'),
    path('new_matiere/',MatiereCreateView.as_view(),name='new.matiere'),
]
