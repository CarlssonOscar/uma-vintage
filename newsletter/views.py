from django.shortcuts import render
from django.http import HttpResponseRedirect


def newsletters(request):

    return render(request, HttpResponseRedirect(request.path_info))
