from django.contrib import admin

# Register your models here.
from .models import Member

@admin.register(Member) # <= using the decorator "register"
class MemberAdmin(admin.ModelAdmin):
    
    list_display = ['firstname','lastname', 'phone']
    pass
