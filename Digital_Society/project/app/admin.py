from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('email','role','isActive','created_at')

class ChairmanAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname')
class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','contact','blockno','houseno')

# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Chairman,ChairmanAdmin)
admin.site.register(Member,MemberAdmin)