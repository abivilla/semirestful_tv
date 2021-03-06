from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.
def re(request):
    return redirect('/shows')

def shows(request):
    context = {
        "all_shows":Show.objects.all()
    }
    return render (request, 'shows.html',context)

def add_show(request):
    
    if request.method == "GET":
        return render (request, 'add_show.html')
    
    else:
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        
            return redirect('/shows/new')
        else:
            show = Show.objects.create(title=request.POST["title"],network=request.POST["network"],release_date=request.POST["release_date"],desc=request.POST["desc"])
        
            return redirect(f'/shows_desc/{show.id}')
    
def shows_desc(request,id):
    show=Show.objects.get(id=id)
    if request.method == "GET":
        context = {
        "show":show
    }
        return render(request,'shows_desc.html',context)

def delete(request,id):
    show=Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')
    
def edit(request,id):
    show=Show.objects.get(id=id)
    if request.method == "GET":
        context = {
        "show":show
    }
        return render(request,'edit.html', context)
    else:
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        
            return redirect(f'/shows/{show.id}/edit')
        else:
            show.title = request.POST["title"]
            show.network = request.POST["network"]
            show.release_date = request.POST["release_date"]
            show.desc= request.POST["desc"]
            show.save()
            return redirect(f'/shows_desc/{show.id}')