from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


