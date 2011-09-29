from django.core.context_processors import csrf
from django.http import Http404
from django.shortcuts import render_to_response, redirect
from heard import settings
from os import listdir
from piece.models import *
from artist.models import *

all_pages = listdir(settings.TEMPLATE_DIRS[0])

def default(request, page):
    if len(Piece.objects.filter(slug = page)) != 0:
        #print 'its a piece page some how'
        piece = Piece.objects.filter(slug = page)[0]
        page = 'sounds.html'
        args = {
            'STATIC_URL' : settings.STATIC_URL,
            'base_template' : "base.html",
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
                'base_template' : "base.html",
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
