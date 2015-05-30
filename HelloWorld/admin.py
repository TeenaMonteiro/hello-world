from django.contrib import admin
from HelloWorld.models import Users


<<<<<<< HEAD

=======
  
>>>>>>> a98ff8aadb705486cbe532470d833d4a9f1747fb
class listusers(admin.ModelAdmin):
    list_display = ('username',"user_create_date")


<<<<<<< HEAD
=======

>>>>>>> a98ff8aadb705486cbe532470d833d4a9f1747fb
admin.site.register(Users,listusers)


