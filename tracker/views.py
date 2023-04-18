from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Opportunity


def home(request):
    return render(request, 'tracker/home.html', {'title': 'Home'})

def customer_project(request):
    context = {
        'opportunities': Opportunity.objects.all()
    }
    return render(request, 'tracker/customer_project.html', context)

class OpportunityListView(ListView):
    model = Opportunity
    template_name = 'tracker/home.html'
    context_object_name = 'opportunities'
    ordering = ['-date_posted']


class OpportunityDetailView(DetailView):
    model = Opportunity
   

class OpportunityCreateView(LoginRequiredMixin,CreateView):
    model = Opportunity
    fields = ['title', 'content']
    success_url = '/customer_project'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class OpportunityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Opportunity
    fields = ['title', 'content']
    success_url = '/customer_project'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        opportunity = self.get_object()
        if self.request.user == opportunity.author:
            return True
        return False
    

class OpportunityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Opportunity
    success_url = '/customer_project'
   
    def test_func(self):
        opportunity = self.get_object()
        if self.request.user == opportunity.author:
            return True
        return False