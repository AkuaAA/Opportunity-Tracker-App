from django.shortcuts import render
from .models import Opportunity


def home(request):
    return render(request, 'tracker/home.html', {'title': 'Home'})

def customer_project(request):
    context = {
        'opportunities': Opportunity.objects.all()
    }
    return render(request, 'tracker/customer_project.html', context)

