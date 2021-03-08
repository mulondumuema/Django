from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homePageView),
    path('about/', views.aboutPageView),
    path('services/', views.servicesPageView),
    path('contact/', views.contactPageView),
]