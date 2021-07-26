from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(["GET","POST"])
def test(request):
    if request.method=="GET":
        return Response({"data":123})
    elif request.method=="POST":
        return Response({"data":123})

