from django.shortcuts import render
from .models import User, Restaurant
from django.views import generic
from django.http import HttpResponse
from django.template import loader

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'restaurants/index.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return User.objects.all().order_by('-first_name')


def signup(request):
    template = loader.get_template('restaurants/signup.html')
    context = {}
    return HttpResponse(template.render(context, request))

def newaccount(request):
    fname = request.POST['first_name']
    lname = request.POST['last_name']
    uname = request.POST['username']
    password = request.POST['password']
    password_conf = request.POST['confirm_password']

    new_user = User(first_name = fname, last_name = lname, username = uname, password = password)
    new_user.save()

    return HttpResponse("User Succesfully Created")
