from django.shortcuts import render
from . import models

def articles_list(request):
    maqalat = models.STATE.objects.all().order_by('date')
    args = {'maqaleh':maqalat}
    return render(request, 'articleslist.html', args)
