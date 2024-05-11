from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='user.home'),
    path('<slug:matiere>/',matiere,name='matiere.vue'),
    path('<slug:matiere>/<slug:cours>/',cours,name='cour.vue'),
]