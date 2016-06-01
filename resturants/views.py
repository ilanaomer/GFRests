from django.shortcuts import render
from django.views import generic
from .models import Restaurant


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'resturants/index.html'
    context_object_name = 'רשימת כל המסעדות'

    def get_queryset(self):
        """Return the last five published questions."""
        return Restaurant.objects.all()

class ResturantView(generic.DetailView):
    model = Restaurant
    template_name = 'resturants/resturant_detail.html'

