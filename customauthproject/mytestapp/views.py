from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index_endpoint(request):
    return render(request, 'mytestapp/index.html', {})


def no_login_required_endpoint(request):
    return HttpResponse("You should have seen this without logging in.")


@login_required
def login_required_endpoint(request):
    return HttpResponse("You should have seen this after logging in.")
