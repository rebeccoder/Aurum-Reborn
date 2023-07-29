from django.shortcuts import render
from creators.models import Creator
from django.http import HttpResponsePermanentRedirect


def index(request):


    return render(request, 'home/index.html')

def home(request):
    creators = Creator.objects.all()
    for c in creators: 
        print(c.name)
    context = {
        'creators': creators,
    }
    return render(request, 'home/index.html', context)

def mobile_home(request):

    return render(request, 'home/mobile-home.html')

def mobile_redirect(request):
    user_agent = request.META['HTTP_USER_AGENT']

    if 'Mobile' in user_agent:
        return redirect('mobile_home')
    else:
        return redirect('home')

def careers(request):
    return render(request, 'home/careers.html')

def returns(request):
    return render(request, 'home/returns.html')

def terms(request):
    return render(request, 'home/terms.html')