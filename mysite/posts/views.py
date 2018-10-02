from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from django.core import serializers
import json


def index(request):
    queryset = Post.objects.all()
    context = {
        "title": "Project list",
        "objects": queryset
    }
    serialized_queryse = serializers.serialize('json', queryset)
    with open('data.json', 'w') as outfile:
        json.dump(serialized_queryse, outfile)
    return HttpResponse(serialized_queryse, content_type='application/json')


