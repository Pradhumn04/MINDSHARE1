from django.contrib import admin
from .models import Room, Topic, Message, User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'name')
    list_display_links = ('username', 'email')
    
admin.site.register(User, UserAdmin)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
