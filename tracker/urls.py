from django.urls import path
from .views import OpportunityListView,OpportunityDetailView, OpportunityCreateView, OpportunityUpdateView, OpportunityDeleteView
from . import views


urlpatterns = [
    path('', OpportunityListView.as_view(), name= 'tracker-home'),
    path('opportunity/<int:pk>/', OpportunityDetailView.as_view(), name='opportunity-detail'),
    path('opportunity/new', OpportunityCreateView.as_view(), name='opportunity-create'),
    path('opportunity/<int:pk>/update/', OpportunityUpdateView.as_view(), name='opportunity-update'),
    path('opportunity/<int:pk>/delete/', OpportunityDeleteView.as_view(), name='opportunity-delete'),
    path('customer_project/', views.customer_project, name='tracker-customer_project'),
]