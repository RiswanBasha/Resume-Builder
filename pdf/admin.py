from django.contrib import admin
from .models import Profile
# Register your models here.

admin.site.site_header="RB's CV Creator Admin"
admin.site.site_title= "RB's CV Creator"
admin.site.index_title= "RB's Manage CV Creator"

admin.site.register(Profile)