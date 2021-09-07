from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your Enumeartion :
Conjonctive = (
    ('normocolorées','normocolorées'),
    ('décolorées','décolorées'),
    ('ictériques','ictériques')
)

ContactèLombaire = (
    ('D','D'),
    ('G','G'),
    ('B','B')
)

Douleur_Masse = (
    ('HD','HD'),
    ('HG','HG'),
    ('EPIG','EPIG'),
    ('FD','FD'),
    ('FG','FG'),
    ('O','O'),
    ('HYPAG','HYPAG')
)

Pleuresie = (
    ('Dplus','Dplus'),
    ('G','G'),
    ('B','B')    
)

Pneumothorax = (
    ('D','D'),
    ('G','G'),
    ('B','B')
)

Retricissement = (
    ('M','M'),
    ('T','T'),
    ('A','A'),
    ('P','P')
)

Rythme = (
    ('régulier','régulier'),
    ('irrégulier','irrégulier')
)

Role = (
    ('assistant','assistant'),
    ('doctor','doctor'),
    ('patient','patient')
)


# Create your models here.
class Person(AbstractUser):
    # attribut form auth_user :
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)    
    email = models.EmailField(verbose_name='email',max_length=50,unique=True)
    password = models.CharField(max_length=1000,default='NullPassword')
    cin = models.CharField(max_length=8)
    date_Birth = models.DateField()
    role = models.CharField(max_length=20,choices=Role,default='patient')
    
    last_login = None
    first_name = None	
    last_name = None
    username = None

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
 

class Profil(models.Model):
    statut = models.IntegerField()
    url_img = models.CharField(max_length=40)
    person = models.ForeignKey(Person, related_name='person', on_delete=models.CASCADE)

class Folder(models.Model) :
    date = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(Person, related_name='patient_Folder', on_delete=models.CASCADE)

class Consultation(models.Model):
    date = models.DateField(auto_now_add=True)
    folder = models.ForeignKey(Folder,related_name='consultations',on_delete=models.CASCADE)
    # d'autres attribut ...

class Appointment(models.Model):
    date = models.DateField()
    time = models.CharField(max_length=5)
    status = models.IntegerField(default=0)
    patient = models.ForeignKey(Person,related_name='patient_appointment',on_delete=models.CASCADE)
    consultation = models.ForeignKey(Consultation,related_name='consultation',on_delete=models.CASCADE,null=True)

class Biological_Exam(models.Model):
    gaj = models.CharField(max_length=200)
    hba1c = models.CharField(max_length=200)
    urée = models.CharField(max_length=200)
    creat = models.CharField(max_length=200)
    nfshb = models.CharField(max_length=200)
    nfsgb = models.CharField(max_length=200)
    nfspq = models.CharField(max_length=200)
    férritinémie = models.CharField(max_length=200)
    asat = models.CharField(max_length=200)
    alat = models.CharField(max_length=200)
    tsh = models.CharField(max_length=200)
    ct = models.CharField(max_length=200)
    tg = models.CharField(max_length=200)
    ldl = models.CharField(max_length=200)
    hdl = models.CharField(max_length=200)
    ecbu = models.CharField(max_length=200)
    vs = models.CharField(max_length=200)
    crp = models.CharField(max_length=200)
    autres = models.CharField(max_length=200)
    consultation = models.ForeignKey(Consultation,related_name='Biological_Exams',on_delete=models.CASCADE)
    

class Radilogical_Exam(models.Model) :
    thorax = models.CharField(max_length=200)
    rx_standard = models.CharField(max_length=200)
    tdm = models.CharField(max_length=200)
    irm = models.CharField(max_length=200)
    consultation = models.ForeignKey(Consultation,related_name='Radilogical_Exams',on_delete=models.CASCADE)
    

class Abdominal_Exam(models.Model) :
    douleur = models.CharField(max_length=10,choices=Douleur_Masse)
    masse = models.CharField(max_length=10,choices=Douleur_Masse)
    ascite = models.BooleanField()
    tympanisme = models.BooleanField()
    distension_tympanique = models.BooleanField()
    hépatomégalie = models.BooleanField()
    splénomégalie = models.BooleanField()
    tr = models.CharField(max_length=200)
    consultation = models.ForeignKey(Consultation,related_name='Abdominal_Exams',on_delete=models.CASCADE)

class Cardio_vasculaire_Exam(models.Model) :
    rythme = models.CharField(max_length=10,choices=Rythme)
    retricissement = models.CharField(max_length=10,choices=Retricissement)
    consultation = models.ForeignKey(Consultation,related_name='Cardio_vasculaire_Exams',on_delete=models.CASCADE)

class Respiratoire_Exam(models.Model) :
    rales_sibilants = models.BooleanField()
    ralents_ronflants = models.CharField(max_length=200)
    pleuresie = models.CharField(max_length=10,choices=Pleuresie)
    pneumothorax = models.CharField(max_length=10,choices=Pneumothorax)
    crépitauts = models.BooleanField()
    consultation = models.ForeignKey(Consultation,related_name='Respiratoire_Exams',on_delete=models.CASCADE)

class Neurologique_Exam(models.Model) :
    normal = models.BooleanField()
    vertige = models.BooleanField()
    autre = models.CharField(max_length=200)
    consultation = models.ForeignKey(Consultation,related_name='Neurologique_Exams',on_delete=models.CASCADE)


class General_Exam(models.Model) :
    ta = models.CharField(max_length=200)
    fc = models.CharField(max_length=200)
    fr = models.CharField(max_length=200)
    t = models.CharField(max_length=200)
    poids = models.CharField(max_length=200)
    taille = models.CharField(max_length=200)
    conjonctive = models.CharField(max_length=20,choices=Conjonctive)
    consultation = models.ForeignKey(Consultation,related_name='General_Exams',on_delete=models.CASCADE)


class Medical_Treatment(models.Model) :
    anti_biotique = models.CharField(max_length=200) 
    anti_inflammatoire = models.CharField(max_length=200) 
    antalgique = models.CharField(max_length=200) 
    anti_spasmodique = models.CharField(max_length=200)
    ipp = models.CharField(max_length=200) 
    anti_émétique = models.CharField(max_length=200) 
    anti_diarrhéique = models.CharField(max_length=200) 
    laxatif = models.CharField(max_length=200) 
    charbon_activé = models.CharField(max_length=200) 
    anti_histaminique = models.CharField(max_length=200) 
    corticotde = models.CharField(max_length=200) 
    anti_hta = models.CharField(max_length=200)  
    b_bloquant = models.CharField(max_length=200) 
    anti_cholestérolémique = models.CharField(max_length=200) 
    ado = models.CharField(max_length=200) 
    insuline = models.CharField(max_length=200) 
    levothyrox = models.CharField(max_length=200)
    dimazol = models.CharField(max_length=200) 
    magnesium = models.CharField(max_length=200) 
    auxiolytique = models.CharField(max_length=200) 
    anti_depresseur = models.CharField(max_length=200) 
    vitamine = models.CharField(max_length=200) 
    anti_mucosique = models.CharField(max_length=200) 
    ctc_local = models.CharField(max_length=200) 
    autres = models.CharField(max_length=200)
    consultation = models.ForeignKey(Consultation,related_name='treatment',on_delete=models.CASCADE)


    