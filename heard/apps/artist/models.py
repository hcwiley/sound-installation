from django.db import models
from django import forms
#from django.core.files import ContentFile
from django.contrib import admin
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Artist(models.Model):
    user = models.ForeignKey(User, unique=True)
    nickname = models.CharField(max_length=400)

    
    def __unicode__(self):
        return slugify(self.user)
        
    def save(self, *args, **kwargs):
        if(self.nickname == None):
            self.nickname = '%s %s' % (self.user.first_name, self.user.last_name)
        super(Artist, self).save(*args, **kwargs)

admin.site.register(Artist)