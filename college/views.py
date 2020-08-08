from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import re
from django.contrib import messages
from django.http import *
from .forms import *
# Create your views here.

def home(request):
    updates = Update.objects.all()
    params = {'update':updates}
    return render(request, 'college/home.html', params)

def aboutus(request):
    return render(request, 'college/aboutus.html')

def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        contact_number = request.POST.get('phone', '')
        contact_number = int(contact_number)
        subject = request.POST.get('subject', '')
        comment = request.POST.get('comment', '')
        max_len = len(str(contact_number))
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        
        try:
            if max_len == 10 and type(contact_number) == int:
                if(re.search(regex,email)):
                    contact = Contact(name=name, email=email, contact_number=contact_number, subject=subject, comment=comment)
                    contact.save()
                else:
                    print("enter corect email")
            else:
                print("enter corect number")
        except:
            return HttpResponseRedirect('/user/already enter that number')
    return render(request, 'college/contactus.html')

def dept(request):
    return render(request, 'college/dept.html')

def gallery(request):
    sport = Sports.objects.all()
    events = Event.objects.all()
    confere = Conferences.objects.all()
    lib = Library.objects.all()
    params = {'sports':sport, 'event':events, 'conferences':confere, 'library':lib}
    return render(request, 'college/gallery.html', params)

def library(request):
    return render(request, 'college/library.html')

def itstaff(request):
    staffs = Staff.objects.all()
    header = "Information Technology Staffs"
    desc = "A Bachelor of Science in Information Technology, (abbreviated BSIT or B.Sc IT), is a Bachelor's degree awarded for an undergraduate course or program in the Information technology field. ... This degree is primarily focused on subjects such as software, databases, and networking."
    n = len(staffs)
    dept = "BSCIT"
    params = {'staff':staffs, 'range':range(n), 'header':header, 'dept':dept, 'desc':desc}
    return render(request, 'college/staff.html', params)

def csstaff(request):
    staffs = Csstaff.objects.all()
    header = "Computer Science Staffs"
    n = len(staffs)
    params = {'staff':staffs, 'range':range(n), 'header':header}
    return render(request, 'college/staff.html', params)

def admission(request):
    return render(request, 'college/admission.html') 

def fyform(request):
    if request.method == 'POST':
        form = FyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully Submited..')
            return HttpResponseRedirect('/fyform/')
    else:
        form = FyForm()
    
    year = 'FY'
    return render(request, 'college/form.html', {'form':form, 'year': year}) 


def syform(request):
    if request.method == 'POST':
        form = SyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully Submited..')
            return HttpResponseRedirect('/syform/')
    else:
        form = SyForm()
    
    year = 'SY'
    return render(request, 'college/form.html', {'form':form, 'year': year}) 


def tyform(request):
    if request.method == 'POST':
        form = TyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully Submited..')
            return HttpResponseRedirect('/tyform/')
    else:
        form = TyForm()
    
    year = 'TY'
    return render(request, 'college/form.html', {'form':form, 'year': year}) 

def syllabus(request):
    return render(request, 'college/syllabus.html')

def nss(request):
    img = Nssimg.objects.all()
    params = {'img':img}
    return render(request, 'college/nss.html', params)



