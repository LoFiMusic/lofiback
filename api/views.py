import datetime
import json
from .models import Music
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from api.serializers import *
import version

@csrf_exempt
def GenPlaylist(request):
        if request.method == 'GET':
            music = Music.objects.all()
            serializer = MusicSerializer(music, many=True)
            return JsonResponse(serializer.data, status=200, safe=False)

        elif request.method == 'POST':
            info = {"Info":"Method not allowed"}
            return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def RandomTrack(request):
    if request.method == 'GET':
        music = Music.objects.order_by('?')[:1]
        serializer = MusicSerializer(music, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

    elif request.method == 'POST':
        info = {"Info":"Method not allowed"}
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def TouchLike(request):
    if request.method == 'POST':
        info = {"Track":"Liked"}
        data = JSONParser().parse(request)
        track = Music.objects.get(id=data['id'])
        track.likes = track.likes+1
        track.save()
        return JsonResponse(info, status=201)

    elif request.method == 'GET':
        info = {"Info":"Method not allowed"}
        return JsonResponse(serializer.errors, status=400)

def Index(request):
        if request.method == 'GET':
            info = {"Status":"Online","version":version.number}
            return JsonResponse(info, status=200, safe=False)
