from django.db import models
from django import forms
from django.conf import settings
#from django.core.files import ContentFile
from django.contrib.admin import widgets 
from django.contrib import admin
from django.template.defaultfilters import slugify
from artist.models import *
import Image
import random

class MyImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    thumb = models.ImageField(upload_to='gallery/', blank=True, null=True, editable=False)
    thumbsize = (250,250)
    
    class Meta:
        ordering = ['image']
        
    def thumb(self):
        return '%s' % self.image.url.replace('gallery/', 'gallery/thumb_')
    
    def __unicode__(self):
        return self.image.url
    
    def saveThumb(self):
        path = '%s/%s' % (settings.MEDIA_ROOT, self.image)
        img = Image.open(path)
        img = img.resize(self.thumbsize, Image.ANTIALIAS)
        path = path.replace('gallery/', 'gallery/thumb_')
        img.save(path)
        self.thumb = path
    
    def save(self, *args, **kwargs):
        super(MyImage, self).save(*args, **kwargs)
        self.saveThumb()
class Sound(models.Model):
    file = models.FileField(upload_to='sounds/')
    
    def save(self, *args, **kwargs):
        super(Sound, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.file.url
class SoundForm(forms.FileField):
    file = forms.FileField(widget=forms.FileInput(), required=False)
    
class Location(models.Model):
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
#    geotag = 

    def __unicode__(self):
        return '%s, %s' % (self.lat, self.long)

class Piece(models.Model):
    title = models.CharField(max_length=400)
    default_image = models.ForeignKey(MyImage, related_name='%(app_label)s_%(class)s_default_image', null=True, blank=True)
    sounds = models.ForeignKey(Sound, related_name='%(app_label)s_%(class)s_sound', null=True, blank=True) 
    slug=models.SlugField(max_length=160,blank=True,editable=False)
    description = models.TextField(null=True, blank=True)
    artist = models.ForeignKey(Artist, null=True, blank=True)
    location = models.ForeignKey(Location, null=True, blank=True)
    show_map = models.BooleanField(default=True)
    use_street_view = models.BooleanField(default=True)
    heading = models.FloatField(default=180.0)
    pitch = models.FloatField(default=0.0)
    zoom = models.FloatField(default=1)
    activation_code = models.CharField(max_length=3, default='000', editable=False, help_text='This what you must type in start audio')
    
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.activation_code == '000' or self.activation_code == '0':
            self.activation_code = '%s%s%s' % (random.randint(0,9),random.randint(0,9),random.randint(0,9))
        super(Piece, self).save(*args, **kwargs)
        
class PieceAdmin(admin.ModelAdmin):
    class Meta:
        model = Piece
    
class PieceForm(forms.ModelForm):
    default_image = forms.ImageField(widget=forms.FileInput(), required=False)
    sounds = SoundForm()
    class Meta:
        model = Piece

admin.site.register(MyImage)
admin.site.register(Sound)
admin.site.register(Location)
admin.site.register(Piece, PieceAdmin)
