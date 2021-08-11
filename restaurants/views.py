from django.shortcuts import render
from .models import User, Restaurant
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse

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

    if password != password_conf:
        return render(request, 'restaurants/signup.html', {
            'error_message': 'Passwords do not Match',
        })

    new_user = User(first_name = fname, last_name = lname, username = uname, password = password)
    new_user.save()

    request.session['user'] = new_user.username
    context = {'user': request.session['user'],}
    template = loader.get_template('restaurants/userhome.html')

    return HttpResponse(template.render(context, request))

def signin(request):
    template = loader.get_template('restaurants/signin.html')
    context = {}
    return HttpResponse(template.render(context, request))

def userhome(request):
    uname = request.POST['username']
    password = request.POST['password']
    request.session['user'] = uname

    try:
        user = User.objects.get(pk=uname)
    except (KeyError, User.DoesNotExist):
        template = loader.get_template('restaurants/signin.html')
        context = {
            'error_message': 'User Does Not Exist',
        }
        return HttpResponseRedirect(reverse('restaurants:signin', args=()))
    else:
        if password != user.password:
            template = loader.get_template('restaurants/signin.html')
            context = {
                'error_message': 'Password is incorrect',
            }
            return HttpResponse(template.render(context, request))
        else:
            context = {'user': request.session['user'],}
            template = loader.get_template('restaurants/userhome.html')

            return HttpResponse(template.render(context, request))
