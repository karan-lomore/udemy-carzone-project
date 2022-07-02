from distutils.command.build_scripts import first_line_re
from distutils.command.upload import upload
from ssl import create_default_context
from venv import create
from django.db import models

class Team(models.Model):
    
    first_name = models.CharField(max_length= 255, blank= False, null= False)
    last_name = models.CharField(max_length= 255, blank= False, null= False)
    designation = models.CharField(max_length= 255, blank= False, null= False)
    photo = models.ImageField(upload_to= 'photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length= 100)
    twitter_link = models.URLField(max_length= 100)
    google_plus_link = models.URLField(max_length= 100)
    created_date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return str(self.first_name)