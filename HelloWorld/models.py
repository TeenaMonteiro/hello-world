from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    user_create_date = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.username

    class Meta:
        db_table = u'users'
