from django.shortcuts import render

from . import models

# Create your views here.
def home(request):
    return render(request, 'base.html')



def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)

    results = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    context = {
        'search': search,
        'results': results
    }
    return render(request, 'recommender/new_search.html', context)