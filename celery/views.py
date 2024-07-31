from django.shortcuts import render, redirect
from .tasks import count_task

def count_to_10(request):
    count_task.delay()
    return redirect('home')
