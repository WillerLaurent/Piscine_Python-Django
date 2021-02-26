from django.shortcuts import render
import psycopg2
from .models import Movies
from django.db import IntegrityError


# Create your views here.
def populate(request):
    result = list()
    try:
        mov1 = Movies(title='The Phantom Menace', director='George Lucas', producer='Rick McCallum',
                      release_date='1999-05-19')
        mov1.save()
        result.append('OK')
    except IntegrityError as e:
        result.append('The Phantom Menace')
        result.append(e)
    try:
        mov1 = Movies(title='Attack of the Clones', director='George Lucas', producer='Rick McCallum',
                      release_date='2002-05-16')
        mov1.save()
        result.append('OK')
    except IntegrityError as e:
        result.append('Attack of the Clones')
        result.append(e)
    try:
        mov1 = Movies(title='Revenge of the Sith', director='George Lucas', producer='Rick McCallum',
                      release_date='2005-05-19')
        mov1.save()
        result.append('OK')
    except IntegrityError as e:
        result.append('Revenge of the Sith')
        result.append(e)
    try:
        mov1 = Movies(title='A New Hope', director='George Lucas', producer='Gary Kurtz, Rick McCallum',
                      release_date='1977-05-25')
        mov1.save()
        result.append('OK')
    except IntegrityError as e:
        result.append('A New Hope')
        result.append(e)
    try:
        mov1 = Movies(title='The Empire Strikes Back', director='Irvin Kershner', producer='Gary Kutz, Rick McCallum',
                      release_date='1980-05-17')
        mov1.save()
        result.append('OK')
    except IntegrityError as e:
        result.append('The Empire Strikes Back')
        result.append(e)
    try:
        mov1 = Movies(title='Return of the Jedi ', director='Richard Marquand',
                      producer='Howard G. Kazanjian, George Lucas, Rick McCallum ', release_date='1983-05-25')
        mov1.save()
        result.append('OK')
    except IntegrityError as e:
        result.append('Return of the Jedi')
        result.append(e)
    try:
        mov1 = Movies(title='The Force Awakens', director='J. J. Abrams',
                      producer='Kathleen Kennedy, J. J. Abrams, Bryan Burk', release_date='2015-12-11')
        mov1.save()
        result.append('OK')
    except IntegrityError as e:
        result.append('The Force Awakens')
        result.append(e)
    return render(request, 'ex02/insert_data.html', {'result': result})


def display(request):
    table = Movies.objects.all()
    return render(request, "ex02/display.html", {'table': table })