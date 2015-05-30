from django.contrib import admin
from HelloWorld.models import Users


  
class listusers(admin.ModelAdmin):
    list_display = ('username',"user_create_date")



admin.site.register(Users,listusers)


