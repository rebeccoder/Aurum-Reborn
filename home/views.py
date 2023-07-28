from django.shortcuts import render
from creators.models import Creator

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