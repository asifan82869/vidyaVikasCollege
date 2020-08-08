from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('dept/', views.dept, name='dept'),
    path('gallery/', views.gallery, name='gallery'),
    path('library/', views.library, name='library'),
    path('itstaff/', views.itstaff, name='itstaff'),
    path('admission/', views.admission, name='admission'),
    path('fyform/', views.fyform, name='fyform'),
    path('syform/', views.syform, name='syform'),
    path('tyform/', views.tyform, name='tyform'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('nss/', views.nss, name='nss'),
]
