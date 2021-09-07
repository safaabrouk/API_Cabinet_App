"""CabinetProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from CabinetApp import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('profil',views.viewsets_Profil)
router.register('person',views.viewsets_Person)

router.register('ae',views.viewsets_Abdominal_Exam)
router.register('be',views.viewsets_Biological_Exam)
router.register('cve',views.viewsets_Cardio_vasculaire_Exam)
router.register('re',views.viewsets_Radilogical_Exam)
router.register('rec',views.viewsets_Respiratoire_Exam)
router.register('ge',views.viewsets_General_Exam)
router.register('ne',views.viewsets_Neurologique_Exam)


router.register('appointment',views.viewsets_Appointment)
router.register('folder',views.viewsets_Folder)
router.register('consultation',views.viewsets_Consultation)
router.register('treatment',views.viewsets_Medical_Treatment)

#router.register('',views.viewsets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]