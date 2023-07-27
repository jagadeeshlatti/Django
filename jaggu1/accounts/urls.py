from django.urls import path
from . import views

urlpatterns=[
    path('about/',views.about),
    path('contact/',views.contact),
    path('facilities/',views.facilities),
    path('',views.home),
    path('dashboard/',views.dashboard),
    path('form/',views.application)
]