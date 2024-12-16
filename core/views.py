from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.conf import settings
import requests


def index(request):
    return render(request, "index.html")

def soon(request):
    return render(request, "comingSoon.html")