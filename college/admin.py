from django.contrib import admin
from college.models import *
# Register your models here.

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'staff_name', 'post','experience','education','joinning_date', 'photo')
    ordering = ('staff_name',)
    search_fields = ('staff_id', 'staff_name', 'post','experience','education','joinning_date')

#admin.site.register(Staff)
admin.site.register(Sports)
admin.site.register(Event)
admin.site.register(Conferences)
admin.site.register(Library)

@admin.register(FYForm)
class FYFormAdmin(admin.ModelAdmin):
    list_display = ('submition_date',
    'id', 
    'image', 
    'first_name', 
    'middle_name', 
    'last_name', 
    'mother_frist_name', 
    'mother_middle_name', 
    'mother_last_name',
    'gender',
    'status',
    'date_of_brith',
    'email',
    'phone1',
    'phone2',
    'current_address',
    'current_city',
    'current_state',
    'current_zip',
    'permanent_address',
    'permanent_city',
    'permanent_state',
    'permanent_zip',
    'year',
    'stream',
    'ssc_school_name',
    'ssc_borad_state',
    'ssc_parcentage',
    'hsc_school_name',
    'hsc_borad_state',
    'hsc_parcentage',
    'ssc_result',
    'hsc_result',
    )
    ordering = ('first_name',)
    search_fields = ('submition_date','id','first_name','middle_name', 'last_name', 'email', 'year', 'stream', 'gender')
#admin.site.register(FYForm)

@admin.register(SYForm)
class SYFormAdmin(admin.ModelAdmin):
    list_display = ('submition_date',
    'id', 
    'image', 
    'first_name', 
    'middle_name', 
    'last_name', 
    'mother_frist_name', 
    'mother_middle_name', 
    'mother_last_name',
    'gender',
    'status',
    'date_of_brith',
    'email',
    'phone1',
    'phone2',
    'current_address',
    'current_city',
    'current_state',
    'current_zip',
    'permanent_address',
    'permanent_city',
    'permanent_state',
    'permanent_zip',
    'year',
    'stream',
    'ssc_school_name',
    'ssc_borad_state',
    'ssc_parcentage',
    'hsc_school_name',
    'hsc_borad_state',
    'hsc_parcentage',
    'sem1_college_name',
    'sem1_university_name',
    'sem1_pointer',
    'sem2_college_name',
    'sem2_university_name',
    'sem2_pointer',
    'ssc_result',
    'hsc_result',
    'sem1_result',
    'sem2_result',
    )
    ordering = ('first_name',)
    search_fields = ('submition_date','id','first_name','middle_name', 'last_name', 'email', 'year', 'stream', 'gender')
#admin.site.register(SYForm)

@admin.register(TYForm)
class TYFormAdmin(admin.ModelAdmin):
    list_display = ('submition_date',
    'id', 
    'image', 
    'first_name', 
    'middle_name', 
    'last_name', 
    'mother_frist_name', 
    'mother_middle_name', 
    'mother_last_name',
    'gender',
    'status',
    'date_of_brith',
    'email',
    'phone1',
    'phone2',
    'current_address',
    'current_city',
    'current_state',
    'current_zip',
    'permanent_address',
    'permanent_city',
    'permanent_state',
    'permanent_zip',
    'year',
    'stream',
    'ssc_school_name',
    'ssc_borad_state',
    'ssc_parcentage',
    'hsc_school_name',
    'hsc_borad_state',
    'hsc_parcentage',
    'sem1_college_name',
    'sem1_university_name',
    'sem1_pointer',
    'sem2_college_name',
    'sem2_university_name',
    'sem2_pointer',
    'sem3_college_name',
    'sem3_university_name',
    'sem3_pointer',
    'sem4_college_name',
    'sem4_university_name',
    'sem4_pointer',
    'ssc_result',
    'hsc_result',
    'sem1_result',
    'sem2_result',
    'sem3_result',
    'sem4_result'
    )
    ordering = ('first_name',)
    search_fields = ('submition_date','id','first_name','middle_name', 'last_name', 'email', 'year', 'stream', 'gender')
#admin.site.register(TYForm)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact_number', 'subject', 'comment')
    ordering = ('name',)
    search_fields = ('name', 'email', 'subject')
#admin.site.register(Contact)

@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('news', 'updations_date')
    ordering = ('news',)
    search_fields = ('news', 'updations_date')
#admin.site.register(Update)

@admin.register(Nssimg)
class NssimgAdmin(admin.ModelAdmin):
    list_display = ('images',)
    ordering = ('images',)
    search_fields = ('images',)
#admin.site.register(Nssimg)