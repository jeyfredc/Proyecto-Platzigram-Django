""" Platzigram views """

# Django
from django.http import HttpResponse
from django.http import JsonResponse

# utilities
from datetime import datetime

def hello_world(request):
    """ Return a greeting """
    return HttpResponse('Oh, hi! current time is {now}'.format(
        now= datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))


def hi(request):
    """ Hi """
    numbers = request.GET['numbers']
    return HttpResponse(sorted(str(numbers).split(',')))


def number(request):
    """ number """
    numbers_string = request.GET['numbers'].split(',')
    numbers_integer = list(map(int, numbers_string))
    numbers_integer.sort()
    return JsonResponse(numbers_integer, safe=False)