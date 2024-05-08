from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required


def index_endpoint(request):
    return render(request, "mytestapp/index.html", {})


def no_login_required_endpoint(request):
    return HttpResponse("You should have seen this without logging in.")


@login_required(login_url="/admin")
def login_required_endpoint(request):
    return HttpResponse("You should have seen this after logging in.")


@permission_required("mytestapp.can_view_permission_required_page", login_url="/admin")
def permission_required_endpoint(request):
    return HttpResponse("You should have seen this if you have permission.")
