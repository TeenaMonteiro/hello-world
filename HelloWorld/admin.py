from django.contrib import admin
from HelloWorld.models import Users


# 
# class UsersInLine(admin.StackedInline):
#   
#     model=Users
  
class listusers(admin.ModelAdmin):
    list_display = ('username',"user_create_date")
#     inlines = [UsersInLine]



# class listusers(admin.ModelAdmin):
# #     date_heirachy = "user_create_date"
#     model=Users


admin.site.register(Users,listusers)


