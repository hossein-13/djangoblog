from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms


def articles_list(request):
    maqalat = models.STATE.objects.all().order_by('-date')
    args = {'maqaleh': maqalat}
    return render(request, 'articleslist.html', args)


def articles_detail(request, slug):
    # return HttpResponse(slug)
    reallist = models.STATE.objects.get(slug=slug)
    return render(request, 'matnslug.html', {'matnbaz': reallist})


@login_required(login_url="/accounts/login")
def create_list(request):
    if request.method == 'POST':
        form = forms.createform(request.POST, request.FILES)
        if form.is_valid:
            return redirect('balahbalh:list')

    else:
        form = forms.createform()
    return render(request, 'create.html', {'formha': form})
