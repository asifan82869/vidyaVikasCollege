from django import forms
from .models import * 
from django.core.validators import validate_email

class FyForm(forms.ModelForm):
    image = forms.ImageField(
    required=True)

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'first name'}
    ), required=True, max_length=20)

    middle_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'middle name'}
    ), required=True, max_length=20)
    
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'last name'}
    ), required=True, max_length=20)
    
    mother_frist_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'mother first name'}
    ), required=True, max_length=20)
    
    mother_middle_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'mother middle name'}
    ), required=True, max_length=20)
    
    mother_last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'mother last name'}
    ), required=True, max_length=20)
    
    gender = forms.ChoiceField(choices=[('male','Male'),('female','FeMale')], required=True)
    
    status = forms.ChoiceField(choices=[('married','Married'),('unmarried','UnMarried')], required=True)
    
    date_of_brith = forms.DateField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'})
        , required=True)
    
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Email'}
    ), required=True,max_length=30)
    
    phone1 = forms.IntegerField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Phone number'}
    ), required=True)
    
    phone2 = forms.IntegerField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Other number'}
    ), required=True)

    current_address = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Current Address'}
    ), required=True, max_length=60)

    current_city = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'City'}
    ), required=True,max_length=20)

    current_state = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'State'}
    ), required=True,max_length=30)

    current_zip = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Zip'}
    ), required=True,max_length=20)

    permanent_address = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Permanent Address'}
    ), required=True,max_length=60)

    permanent_city = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'City'}
    ), required=True,max_length=20)

    permanent_state = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'State'}
    ), required=True,max_length=30)

    permanent_zip = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Zip'}
    ), required=True,max_length=20)

    stream = forms.ChoiceField(choices=[('B.Sc.IT','B.Sc.IT'),('B.Sc.CS','B.Sc.CS'),('BMS','BMS'),('BCOM','BCOM'),('BAF','BAF'),('B.Sc.BIO','B.Sc.BIO')], required=True)

    ssc_school_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    ssc_borad_state = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    ssc_parcentage = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    hsc_school_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    hsc_borad_state = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    hsc_parcentage = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    
    ssc_result = forms.ImageField(required=True)
    hsc_result = forms.ImageField(required=True)
    
    
    class Meta():
        model = FYForm
        fields = ['image', 'first_name', 'middle_name', 'last_name', 'mother_frist_name', 
        'mother_middle_name', 'mother_last_name', 'gender', 'status', 'date_of_brith', 'email', 'phone1', 'phone2',
        'current_address', 'current_city', 'current_state', 'current_zip', 'permanent_address', 'permanent_city', 'permanent_state',
        'permanent_zip', 'stream', 'ssc_school_name', 'ssc_borad_state', 'ssc_parcentage', 'hsc_school_name',
        'hsc_borad_state', 'hsc_parcentage', 'ssc_result', 'hsc_result']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            mt = validate_email(email)
        except:
            raise forms.ValidationError("Enter a corrct Email")
        return email
    
    def clean_phone1(self):
        phone = self.cleaned_data['phone1']
        if len(str(phone)) != 10:
            raise forms.ValidationError("Enter a corrct phone number")
    
    def clean_phone2(self):
        phone = self.cleaned_data['phone2']
        if len(str(phone)) != 10:
            raise forms.ValidationError("Enter a corrct phone number")

class SyForm(forms.ModelForm):
    image = forms.ImageField(
    required=True)

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'first name'}
    ), required=True, max_length=20)

    middle_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'middle name'}
    ), required=True, max_length=20)
    
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'last name'}
    ), required=True, max_length=20)
    
    mother_frist_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'mother first name'}
    ), required=True, max_length=20)
    
    mother_middle_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'mother middle name'}
    ), required=True, max_length=20)
    
    mother_last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'mother last name'}
    ), required=True, max_length=20)
    
    gender = forms.ChoiceField(choices=[('male','Male'),('female','FeMale')], required=True)
    
    status = forms.ChoiceField(choices=[('married','Married'),('unmarried','UnMarried')], required=True)
    
    date_of_brith = forms.DateField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'})
        , required=True)
    
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Email'}
    ), required=True,max_length=30)
    
    phone1 = forms.IntegerField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Phone number'}
    ), required=True)
    
    phone2 = forms.IntegerField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Other number'}
    ), required=True)

    current_address = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Current Address'}
    ), required=True, max_length=60)

    current_city = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'City'}
    ), required=True,max_length=20)

    current_state = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'State'}
    ), required=True,max_length=30)

    current_zip = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Zip'}
    ), required=True,max_length=20)

    permanent_address = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Permanent Address'}
    ), required=True,max_length=60)

    permanent_city = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'City'}
    ), required=True,max_length=20)

    permanent_state = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'State'}
    ), required=True,max_length=30)

    permanent_zip = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Zip'}
    ), required=True,max_length=20)

    stream = forms.ChoiceField(choices=[('B.Sc.IT','B.Sc.IT'),('B.Sc.CS','B.Sc.CS'),('BMS','BMS'),('BCOM','BCOM'),('BAF','BAF'),('B.Sc.BIO','B.Sc.BIO')], required=True)

    ssc_school_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    ssc_borad_state = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    ssc_parcentage = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    hsc_school_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    hsc_borad_state = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    hsc_parcentage = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    sem1_college_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True , max_length=30)

    sem1_university_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    sem1_pointer = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    sem2_college_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    sem2_university_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    sem2_pointer = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    sem3_college_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)


    ssc_result = forms.ImageField(required=True)
    hsc_result = forms.ImageField(required=True)
    sem1_result = forms.ImageField(required=True)
    sem2_result = forms.ImageField(required=True)

    
    class Meta():
        model = SYForm
        fields = ['image', 'first_name', 'middle_name', 'last_name', 'mother_frist_name', 
        'mother_middle_name', 'mother_last_name', 'gender', 'status', 'date_of_brith', 'email', 'phone1', 'phone2',
        'current_address', 'current_city', 'current_state', 'current_zip', 'permanent_address', 'permanent_city', 'permanent_state',
        'permanent_zip', 'stream', 'ssc_school_name', 'ssc_borad_state', 'ssc_parcentage', 'hsc_school_name',
        'hsc_borad_state', 'hsc_parcentage', 'sem1_college_name', 'sem1_university_name', 'sem1_pointer', 
        'sem2_college_name', 'sem2_university_name', 'sem2_pointer', 'ssc_result', 'hsc_result', 'sem1_result',
        'sem2_result']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            mt = validate_email(email)
        except:
            raise forms.ValidationError("Enter a corrct Email")
        return email
    
    def clean_phone1(self):
        phone = self.cleaned_data['phone1']
        if len(str(phone)) != 10:
            raise forms.ValidationError("Enter a corrct phone number")
    
    def clean_phone2(self):
        phone = self.cleaned_data['phone2']
        if len(str(phone)) != 10:
            raise forms.ValidationError("Enter a corrct phone number")


class TyForm(forms.ModelForm):
    image = forms.ImageField(
    required=True)

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'first name'}
    ), required=True, max_length=20)

    middle_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'middle name'}
    ), required=True, max_length=20)
    
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'last name'}
    ), required=True, max_length=20)
    
    mother_frist_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'mother first name'}
    ), required=True, max_length=20)
    
    mother_middle_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'mother middle name'}
    ), required=True, max_length=20)
    
    mother_last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'mother last name'}
    ), required=True, max_length=20)
    
    gender = forms.ChoiceField(choices=[('male','Male'),('female','FeMale')], required=True)
    
    status = forms.ChoiceField(choices=[('married','Married'),('unmarried','UnMarried')], required=True)
    
    date_of_brith = forms.DateField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'})
        , required=True)
    
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Email'}
    ), required=True,max_length=30)
    
    phone1 = forms.IntegerField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Phone number'}
    ), required=True)
    
    phone2 = forms.IntegerField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Other number'}
    ), required=True)

    current_address = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Current Address'}
    ), required=True, max_length=60)

    current_city = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'City'}
    ), required=True,max_length=20)

    current_state = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'State'}
    ), required=True,max_length=30)

    current_zip = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Zip'}
    ), required=True,max_length=20)

    permanent_address = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Permanent Address'}
    ), required=True,max_length=60)

    permanent_city = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'City'}
    ), required=True,max_length=20)

    permanent_state = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'State'}
    ), required=True,max_length=30)

    permanent_zip = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Zip'}
    ), required=True,max_length=20)

    stream = forms.ChoiceField(choices=[('B.Sc.IT','B.Sc.IT'),('B.Sc.CS','B.Sc.CS'),('BMS','BMS'),('BCOM','BCOM'),('BAF','BAF'),('B.Sc.BIO','B.Sc.BIO')], required=True)

    ssc_school_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    ssc_borad_state = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    ssc_parcentage = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    hsc_school_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    hsc_borad_state = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    hsc_parcentage = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    sem1_college_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True , max_length=30)

    sem1_university_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    sem1_pointer = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    sem2_college_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    sem2_university_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    sem2_pointer = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    sem3_college_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    sem3_university_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    sem3_pointer = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    sem4_college_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    sem4_university_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    sem4_pointer = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), required=True,max_length=30)

    ssc_result = forms.ImageField(required=True)
    hsc_result = forms.ImageField(required=True)
    sem1_result = forms.ImageField(required=True)
    sem2_result = forms.ImageField(required=True)
    sem3_result = forms.ImageField(required=True)
    sem4_result = forms.ImageField(required=True)
    
    class Meta():
        model = TYForm
        fields = ['image', 'first_name', 'middle_name', 'last_name', 'mother_frist_name', 
        'mother_middle_name', 'mother_last_name', 'gender', 'status', 'date_of_brith', 'email', 'phone1', 'phone2',
        'current_address', 'current_city', 'current_state', 'current_zip', 'permanent_address', 'permanent_city', 'permanent_state',
        'permanent_zip', 'stream', 'ssc_school_name', 'ssc_borad_state', 'ssc_parcentage', 'hsc_school_name',
        'hsc_borad_state', 'hsc_parcentage', 'sem1_college_name', 'sem1_university_name', 'sem1_pointer', 
        'sem2_college_name', 'sem2_university_name', 'sem2_pointer', 'sem3_college_name', 'sem3_university_name', 'sem3_pointer',
        'sem4_college_name', 'sem4_university_name', 'sem4_pointer', 'ssc_result', 'hsc_result', 'sem1_result',
        'sem2_result', 'sem3_result', 'sem4_result']

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            mt = validate_email(email)
        except:
            raise forms.ValidationError("Enter a corrct Email")
        return email
    
    def clean_phone1(self):
        phone = self.cleaned_data['phone1']
        if len(str(phone)) != 10:
            raise forms.ValidationError("Enter a corrct phone number")
    
    def clean_phone2(self):
        phone = self.cleaned_data['phone2']
        if len(str(phone)) != 10:
            raise forms.ValidationError("Enter a corrct phone number")