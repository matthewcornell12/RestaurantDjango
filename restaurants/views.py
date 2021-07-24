from django.shortcuts import render
from .models import User, Restaurant
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    model = User
    template_name = 'restaurants/index.html'

    def get_quesryset(self):
        return User.objects.all().order_by('-first_name')
