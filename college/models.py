from django.db import models
from datetime import datetime

# Create your models here.
class Staff (models.Model):
    staff_id = models.CharField(max_length=50, unique=True)
    staff_name = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    joinning_date = models.DateField()
    depatment = models.CharField(max_length=20, default = '')
    photo = models.ImageField(upload_to="college/staff", null=True, blank=True)

class Sports (models.Model):
    name = models.CharField(max_length=50, default="sport-img")
    sport = models.ImageField(upload_to="college/sport")
    def __str__(self):
        return f"{self.name}" 

class Event (models.Model):
    name = models.CharField(max_length=50, default="event-img")
    event = models.ImageField(upload_to="college/event")
    def __str__(self):
        return f"{self.name}" 

class Conferences (models.Model):
    name = models.CharField(max_length=50, default="Conferences-img")
    conferences = models.ImageField(upload_to="college/conference")
    def __str__(self):
        return f"{self.name}" 

class Library (models.Model):
    name = models.CharField(max_length=50, default="Library-img") 
    library = models.ImageField(upload_to="college/library")
    def __str__(self):
        return f"{self.name}" 

class Update (models.Model):
    news = models.TextField()
    updations_date = models.DateField()

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact_number = models.IntegerField(unique=True)                  
    subject = models.CharField(max_length=50)
    comment = models.CharField(max_length=5000)

class FYForm(models.Model):
    submition_date = models.DateField(auto_now=True)
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="college/form/image")
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mother_frist_name = models.CharField(max_length=50)
    mother_middle_name = models.CharField(max_length=50)
    mother_last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    date_of_brith = models.DateField()
    email = models.CharField(max_length=50)
    phone1 = models.IntegerField()
    phone2 = models.IntegerField()
    current_address = models.CharField(max_length=50)
    current_city = models.CharField(max_length=50)
    current_state = models.CharField(max_length=50)
    current_zip = models.CharField(max_length=20)
    permanent_address = models.CharField(max_length=50)
    permanent_city = models.CharField(max_length=50)
    permanent_state = models.CharField(max_length=50)
    permanent_zip = models.CharField(max_length=20)
    year = models.CharField(max_length=20, default="FY")
    stream = models.CharField(max_length=20)
    ssc_school_name = models.CharField(max_length=50)
    ssc_borad_state = models.CharField(max_length=50)
    ssc_parcentage = models.CharField(max_length=50)
    hsc_school_name = models.CharField(max_length=50)
    hsc_borad_state = models.CharField(max_length=50)
    hsc_parcentage = models.CharField(max_length=50)
    ssc_result = models.ImageField(upload_to="college/form/result", default='')
    hsc_result = models.ImageField(upload_to="college/form/result", default='')
    
class SYForm(models.Model):
    submition_date = models.DateField(auto_now=True)
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="college/form/image")
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mother_frist_name = models.CharField(max_length=50)
    mother_middle_name = models.CharField(max_length=50)
    mother_last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    date_of_brith = models.DateField()
    email = models.CharField(max_length=50)
    phone1 = models.IntegerField()
    phone2 = models.IntegerField()
    current_address = models.CharField(max_length=50)
    current_city = models.CharField(max_length=50)
    current_state = models.CharField(max_length=50)
    current_zip = models.CharField(max_length=20)
    permanent_address = models.CharField(max_length=50)
    permanent_city = models.CharField(max_length=50)
    permanent_state = models.CharField(max_length=50)
    permanent_zip = models.CharField(max_length=20)
    year = models.CharField(max_length=20, default="SY")
    stream = models.CharField(max_length=20)
    ssc_school_name = models.CharField(max_length=50)
    ssc_borad_state = models.CharField(max_length=50)
    ssc_parcentage = models.CharField(max_length=50)
    hsc_school_name = models.CharField(max_length=50)
    hsc_borad_state = models.CharField(max_length=50)
    hsc_parcentage = models.CharField(max_length=50)
    sem1_college_name = models.CharField(max_length=50, null=True, blank=True)
    sem1_university_name = models.CharField(max_length=50, null=True, blank=True)
    sem1_pointer = models.CharField(max_length=50, null=True, blank=True)
    sem2_college_name = models.CharField(max_length=50, null=True, blank=True)
    sem2_university_name = models.CharField(max_length=50, null=True, blank=True)
    sem2_pointer = models.CharField(max_length=50, null=True, blank=True)
    sem3_college_name = models.CharField(max_length=50, null=True, blank=True)
    ssc_result = models.ImageField(upload_to="college/form/result")
    hsc_result = models.ImageField(upload_to="college/form/result")
    sem1_result = models.ImageField(upload_to="college/form/result")
    sem2_result = models.ImageField(upload_to="college/form/result")
   
class TYForm(models.Model):
    submition_date = models.DateField(auto_now=True)
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="college/form/image")
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mother_frist_name = models.CharField(max_length=50)
    mother_middle_name = models.CharField(max_length=50)
    mother_last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    date_of_brith = models.DateField()
    email = models.CharField(max_length=50)
    phone1 = models.IntegerField()
    phone2 = models.IntegerField()
    current_address = models.CharField(max_length=50)
    current_city = models.CharField(max_length=50)
    current_state = models.CharField(max_length=50)
    current_zip = models.CharField(max_length=20)
    permanent_address = models.CharField(max_length=50)
    permanent_city = models.CharField(max_length=50)
    permanent_state = models.CharField(max_length=50)
    permanent_zip = models.CharField(max_length=20)
    year = models.CharField(max_length=20, default="TY")
    stream = models.CharField(max_length=20)
    ssc_school_name = models.CharField(max_length=50)
    ssc_borad_state = models.CharField(max_length=50)
    ssc_parcentage = models.CharField(max_length=50)
    hsc_school_name = models.CharField(max_length=50)
    hsc_borad_state = models.CharField(max_length=50)
    hsc_parcentage = models.CharField(max_length=50)
    sem1_college_name = models.CharField(max_length=50, null=True, blank=True)
    sem1_university_name = models.CharField(max_length=50, null=True, blank=True)
    sem1_pointer = models.CharField(max_length=50, null=True, blank=True)
    sem2_college_name = models.CharField(max_length=50, null=True, blank=True)
    sem2_university_name = models.CharField(max_length=50, null=True, blank=True)
    sem2_pointer = models.CharField(max_length=50, null=True, blank=True)
    sem3_college_name = models.CharField(max_length=50, null=True, blank=True)
    sem3_university_name = models.CharField(max_length=50, null=True, blank=True)
    sem3_pointer = models.CharField(max_length=50, null=True, blank=True)
    sem4_college_name = models.CharField(max_length=50, null=True, blank=True)
    sem4_university_name = models.CharField(max_length=50, null=True, blank=True)
    sem4_pointer = models.CharField(max_length=50, null=True, blank=True)
    ssc_result = models.ImageField(upload_to="college/form/result", default='')
    hsc_result = models.ImageField(upload_to="college/form/result", default='')
    sem1_result = models.ImageField(upload_to="college/form/result", default='')
    sem2_result = models.ImageField(upload_to="college/form/result", default='')
    sem3_result = models.ImageField(upload_to="college/form/result", default='')
    sem4_result = models.ImageField(upload_to="college/form/result", default='')

class Nssimg(models.Model):
    images = models.ImageField(upload_to="college/Nss")

    
    
    