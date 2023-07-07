from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class StuAdmin(UserAdmin):
     model = CustomUser
     list_display = (
        'username', 'email', 'first_name', 'last_name', 'prof',
    )
     fieldsets = (
        (None, {'fields': ('email', 'password', 'prof')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
admin.site.register(CustomUser, StuAdmin)
admin.site.register(Language)
admin.site.register(School)
admin.site.register(Category)
admin.site.register(Director)
admin.site.register(Code_and_Name_discipline)
admin.site.register(ECTS_and_hours)
admin.site.register(Prerequisites)
admin.site.register(TrainingLevel)
admin.site.register(Semester)
admin.site.register(EduPrograms)
admin.site.register(Language_of_education)
admin.site.register(Proficiency_level)
admin.site.register(Format_of_training)
admin.site.register(Instructor)
admin.site.register(Contact)
admin.site.register(Time_Place)
