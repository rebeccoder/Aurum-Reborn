from django.shortcuts import render
from creators.models import Creator
from django.http import HttpResponsePermanentRedirect


# Create your views here.
def index(request):
    """ A View to reutn the index page """

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
    # Your logic to render the mobile home page goes here
    return render(request, 'home/mobile-home.html')

def mobile_redirect(request):
    user_agent = request.META['HTTP_USER_AGENT']

    # Check if the user is on a mobile device
    if 'Mobile' in user_agent:
        return redirect('mobile_home')
    else:
        return redirect('home')