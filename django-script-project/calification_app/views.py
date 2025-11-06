from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# Create your views here.
from .models import Calification


califications = Calification.objects.all()

def all_califications(request):
    context = {'califications': califications}
    return render(request, 'all_califications.html', context)

def index(request):
    return render(request, 'index.html')

def calificate(request):
    if request.method == "POST":
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')
        calification_date = request.POST.get('calification_date')

        if name and comment and rating and calification_date:
            calification = Calification(
                name=name,
                comment=comment,
                rating=int(rating),
                calification_date= calification_date
            )
            calification.save()
        else:
            print("Missing fields!")
    context = {'califications': califications}
    return render(request, 'all_califications.html', context)


