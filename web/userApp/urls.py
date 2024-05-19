from django.urls import path
from .views import *
app_name="user"
urlpatterns = [
    path('',home,name='home'),
    path('<slug:matiere>/',matiere,name='matiere.vue'),
    path('<slug:matiere>/<slug:cours>/',cours,name='cour.vue'),
]