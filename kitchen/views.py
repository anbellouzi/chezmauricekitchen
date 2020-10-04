from django.views.generic.list import ListView
from django.shortcuts import render

# Create your views here.

class HomePage(ListView):
    def get(self, request):
        return render(request, 'index.html')
