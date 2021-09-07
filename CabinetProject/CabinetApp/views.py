from .models import *
from django.shortcuts import render
from rest_framework import viewsets,status 
from rest_framework.response import Response
from .serializers import *

# Create your views here.
class viewsets_Person(viewsets.ModelViewSet) :
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class viewsets_Profil(viewsets.ModelViewSet) :
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer
    

class  viewsets_Consultation(viewsets.ModelViewSet) :
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer


class  viewsets_Appointment(viewsets.ModelViewSet) :
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class  viewsets_Folder(viewsets.ModelViewSet) :
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class  viewsets_Biological_Exam(viewsets.ModelViewSet) :
    queryset = Biological_Exam.objects.all()
    serializer_class = Biological_ExamSerializer
    

class  viewsets_Radilogical_Exam(viewsets.ModelViewSet) :
    queryset = Radilogical_Exam.objects.all()
    serializer_class = Radilogical_ExamSerializer
    

class  viewsets_Abdominal_Exam(viewsets.ModelViewSet) :
    queryset = Abdominal_Exam.objects.all()
    serializer_class = Abdominal_ExamSerializer


class  viewsets_Cardio_vasculaire_Exam(viewsets.ModelViewSet) :
    queryset = Cardio_vasculaire_Exam.objects.all()
    serializer_class = Cardio_vasculaire_ExamSerializer


class  viewsets_Respiratoire_Exam(viewsets.ModelViewSet) :
    queryset = Respiratoire_Exam.objects.all()
    serializer_class = Respiratoire_ExamSerializer


class  viewsets_Neurologique_Exam(viewsets.ModelViewSet) :
    queryset = Neurologique_Exam.objects.all()
    serializer_class = Neurologique_ExamSerializer


class viewsets_General_Exam(viewsets.ModelViewSet) :
    queryset = General_Exam.objects.all()
    serializer_class = General_ExamSerializer


class viewsets_Medical_Treatment(viewsets.ModelViewSet) :
    queryset = Medical_Treatment.objects.all()
    serializer_class = Medical_TreatmentSerializer