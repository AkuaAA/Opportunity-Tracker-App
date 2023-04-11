from django.shortcuts import render

opportunities = [
    {
        'author': 't-aapeagyei',
        'title': 'NHS Logic Apps',
        'content': 'Join the DevOps Squad hackathon to create a logic app!',
        'date_posted': 'April 03/04/2023'
    },
    {
        'author': 't-aapeagyei',
        'title': 'Power Apps Mip',
        'content': 'Present a 3 day Power App Mip to TFL',
        'date_posted': 'April 04/04/2023'
    }
]

def home(request):
    return render(request, 'tracker/home.html', {'title': 'Home'})

def customer_project(request):
    context = {
        'opportunities': opportunities
    }
    return render(request, 'tracker/customer_project.html', context)

