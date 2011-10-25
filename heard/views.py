from django.core.context_processors import csrf
from django.http import Http404
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.admin import User
from django.contrib import auth
from heard import settings
from os import listdir
from piece.models import *
from artist.models import *

all_pages = listdir(settings.TEMPLATE_DIRS[0])

def edit(request, page):
    if request.user.is_authenticated():
        if len(Piece.objects.filter(slug = page)) != 0:
            #print 'its a piece page some how'
            piece = Piece.objects.filter(slug = page)[0]
            page = 'sounds.html'
            args = {
                'STATIC_URL' : settings.STATIC_URL,
                'base_template' : "edit.html",
                'artists' : Artist.objects.all(),
                'sounds' : Piece.objects.all(),
                'sound' : piece,
                'sound_form' : PieceForm(instance=piece),
                'page': page,
            }
            args.update(csrf(request))
            return render_to_response('sounds.html', args)
        if page.endswith('/'):
                return check_without_slash(request, page)
        if 'html' not in page:
            page = '%s.html' % page
        if page in all_pages:
            args = {
                    'STATIC_URL' : settings.STATIC_URL,
                    'base_template' : "edit.html",
                    'artists' : Artist.objects.all(),
                    'sounds' : Piece.objects.all(),
                    'piece_form' : PieceForm(),
                    'page': page
            }
            args.update(csrf(request))
            return render_to_response(page, args)
    else:
        args = {
            'STATIC_URL' : settings.STATIC_URL,
            'artists' : Artist.objects.all(),
            'sounds' : Piece.objects.all(),
            }
        args.update(csrf(request))
        return render_to_response('not-logged-in.html', args)

def default(request, page):
    if len(Piece.objects.filter(slug = page)) != 0:
        #print 'its a piece page some how'
        piece = Piece.objects.filter(slug = page)[0]
        page = 'sounds.html'
        args = {
            'STATIC_URL' : settings.STATIC_URL,
            'base_template' : "default.html",
            'artists' : Artist.objects.all(),
            'sounds' : Piece.objects.all(),
            'sound' : piece,
            'page': page,
        }
        args.update(csrf(request))
        return render_to_response('sounds.html', args)
    if 'html' not in page:
        page = '%s.html' % page
    if page in all_pages:
        args = {
                'STATIC_URL' : settings.STATIC_URL,
                'base_template' : "default.html",
                'artists' : Artist.objects.all(),
                'sounds' : Piece.objects.all(),
                'page': page
                }
        args.update(csrf(request))
        if page.endswith('/'):
            return check_without_slash(request, page)
        return render_to_response(page, args)
    else:
        raise Http404


def get(request, page):
    if not request.is_ajax():
        raise Http404
    args = {
            'STATIC_URL' : settings.STATIC_URL,
            'base_template' : "base-ajax.html",
            }
    args.update(csrf(request))
    if page.endswith('/'):
        page = page[:-1]
    if page == '':
        page = 'home'
    page = "%s.html" % page
    if page in all_pages:
        return render_to_response('%s' % page, args)
    else:
        raise Http404

def check_without_slash(request, page):
    return redirect('views.default', page = page.rstrip('/'))

def login(request):
    usern = request.POST['username']
    passw = request.POST['password']
    user = auth.authenticate(username = usern, password = passw)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return redirect('views.edit', page = 'home')
    else:
        # Show an error page
        args = {
                'user': request.user,
                }
        args.update(csrf(request))
        return render_to_response('not-logged-in.html', args)
def logout(request):
    auth.logout(request)
    args = {
            'user': request.user,
    }
    args.update(csrf(request))
    # Redirect to a success page.
    return render_to_response('not-logged-in.html', args)

def add_piece(request):
    if request.method != "POST":
        raise Http404
    try:
        lat = request.POST['lat']
        long = request.POST['long']
        img = ''
        sound = ''
        if 'sounds' in request.FILES:
            sound = request.FILES['sounds']
        if 'default_image' in request.FILES:
            img = request.FILES['default_image']
        piece = Piece.objects.create()
        title = request.POST['title']
        piece.title = title
        if request.POST['description'] != '':
            description = request.POST['description']
            piece.description = description
        loc = Location.objects.create()
        loc.lat = lat
        loc.long = long
        loc.save()
        piece.location = loc
        print piece.location
        if img != '':
            image = MyImage.objects.create(image=img)
            image.save()
            piece.default_image = image
        if sound != '':
            sounds = Sound.objects.create(file=sound)
            sounds.save()
            piece.sounds = sounds
        artist = Artist.objects.get(user=User.objects.get(username=request.user))
        piece.artist = artist
        piece.save()
        piece = Piece.objects.get(title=title)
        page = 'sounds.html'
        args = {
            'STATIC_URL' : settings.STATIC_URL,
            'base_template' : "default.html",
            'artists' : Artist.objects.all(),
            'sounds' : Piece.objects.all(),
            'sound' : piece,
            'page': page,
        }
        args.update(csrf(request))
        return render_to_response('sounds.html', args)
    except:
        print 'bad form'
        return HttpResponseNotFound("invalid form")
    
def save_street(request):
    if request.method != "POST":
        raise Http404
    try:
        sound = Piece.objects.get(title=request.POST['title'])
        sound.heading = request.POST['heading']
        sound.pitch = request.POST['pitch']
        sound.zoom = request.POST['zoom']
        sound.save()
        return HttpResponse("big score")
    except:
        print 'bad form'
        return HttpResponseNotFound("invalid form")
    
def save_location(request):
    if request.method != "POST":
        raise Http404
    try:
        sound = Piece.objects.get(pk=request.POST['pk'])
        print sound
        location = sound.location
        print location
        location.lat = request.POST['lat']
        location.long = request.POST['long']
        location.save()
        print location
        sound.location = location
        print sound.location
        sound.save()
        return HttpResponse("big score")
    except:
        print 'bad form'
        return HttpResponseNotFound("invalid form")