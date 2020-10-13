""" Platzigram views """

# Django
from django.http import HttpResponse

# utilities
from datetime import datetime
import json

def hello_world(request):
    """ Return a greeting """
    return HttpResponse('Oh, hi! current time is {now}'.format(
        now= datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))


def sort_integers(request):
    """ Returna JSON response with sorted integers. """
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfuly.'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def say_hi(request, name, age):
    """ Return a greeting """
    if age < 15:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)