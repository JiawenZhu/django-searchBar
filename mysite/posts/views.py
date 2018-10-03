from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from django.core import serializers
import json


def index(request):
    queryset = Post.objects.all()
    # can alsos display this data on index.html as well
    # context = {
    #     "title": "Project list",
    #     "objects": queryset
    # }
    serialized_queryse = serializers.serialize('json', queryset)
    # creating json file
    with open('data.json', 'w') as outfile:
        json.dump(serialized_queryse, outfile)

    # display data at http://127.0.0.1:8000/posts
    return HttpResponse(serialized_queryse, content_type='application/json')


