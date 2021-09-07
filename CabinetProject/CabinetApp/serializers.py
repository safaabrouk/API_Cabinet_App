from rest_framework import serializers
from .models import *

class ProfilSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Profil
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer) :
    
    class Meta :
        model = Person
        fields = '__all__'
        depth = 1


class AppointmentSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Appointment
        fields = '__all__'

class Biological_ExamSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Biological_Exam
        fields = '__all__'
    

class Radilogical_ExamSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Respiratoire_Exam
        fields = '__all__'
    

class Abdominal_ExamSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Abdominal_Exam
        fields = '__all__'

class Cardio_vasculaire_ExamSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Cardio_vasculaire_Exam
        fields = '__all__'

class Respiratoire_ExamSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Respiratoire_Exam
        fields = '__all__'

class Neurologique_ExamSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Neurologique_Exam
        fields = '__all__'


class General_ExamSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = General_Exam
        fields = '__all__'


class Medical_TreatmentSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Medical_Treatment
        fields = '__all__'



class ConsultationSerializer(serializers.ModelSerializer) :
    BC = Biological_ExamSerializer(
        many=True, 
        read_only=True
    )
    RC = Radilogical_ExamSerializer(
        many=True, 
        read_only=True
    )
    AC = Abdominal_ExamSerializer(
        many=True, 
        read_only=True
    )
    CVC = Cardio_vasculaire_ExamSerializer(
        many=True, 
        read_only=True
    )
    ReC =  Respiratoire_ExamSerializer(
        many=True, 
        read_only=True
    )
    NC = Neurologique_ExamSerializer(
        many=True, 
        read_only=True
    )
    GC = General_ExamSerializer(
        many=True, 
        read_only=True
    )
    treatment = Medical_TreatmentSerializer(
        many=True, 
        read_only=True
    )
    class Meta :
        model = Consultation
        fields = ['id','Date','Biological_Exams','Radilogical_Exams','Abdominal_Exams',
        'Cardio_vasculaire_Exams','Respiratoire_Exams','Neurologique_Exams','General_Exams','treatment']

class FolderSerializer(serializers.ModelSerializer) :
    consultations = ConsultationSerializer(
        many=True, 
        read_only=True
    )
    class Meta :
        model = Folder
        fields = ['id','patient','consultations']
        depth = 1