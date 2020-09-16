from django.contrib import admin
from .models import StudentInfo, JobInfo, EventInfo, CompanyInfo

# Register your models here.
admin.site.register(StudentInfo)
admin.site.register(JobInfo)
admin.site.register(EventInfo)
admin.site.register(CompanyInfo)
