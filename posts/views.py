"""Post views.  """

# Django
from django.shortcuts import render
from datetime import datetime


posts=[
    {
        'title': 'Mont Blanck',
        'user': {
            'name': 'Jeyfred Calderon',
            'picture': 'https://lh3.googleusercontent.com/ogw/ADGmqu9Rq5ukqaEtLja_pDNAyZJq7qMy3YTdwSEEdhXF=s32-c-mo',
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60?image=1005',
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (Thespianartist)',
            'picture': 'https://picsum.photos/60/60?image=883',
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700?image=1076',
    },
]


def list_posts(request):
    """ List existing posts. """
    return render(request, 'feed.html', {'posts': posts})
