from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

#CBW - Class Based Views

#FBW - Function Based Views

@api_view(["GET"])
def hello_world(request):
    data = {"info":"Dobredojdovte vo Django"}
    return Response(data)


# DRF - Django Rest Framework