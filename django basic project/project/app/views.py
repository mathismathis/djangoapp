from django.shortcuts import render,redirect
from .models import webdata
from .forms import frontform


def webpage(request):
    form = frontform()
    if request.method == 'POST':
        form = frontform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/retrieve')

    return render(request,'base.html',{'form':form})
def retrieve(request):
    view=webdata.objects.all()
    return render(request,'retire.html',{'view':view})


def update(request):
    view = frontform()

    if request.method == 'POST':
        form = frontform(request.POST)
        if form.is_valid():

            form.save()
            return redirect('/retrieve')


    return render(request,'update.html',{'view':view})

def delete(request, id):
   emp = webdata.objects.get(pk = id)
   emp.delete()
   return redirect('/retrieve')


def updateid(request, id):
    emp = webdata.objects.get(pk = id)

    if request.method == 'POST':
        form = frontform(request.POST,instance=emp)
        print("hi")
        if form.is_valid():
            form.save()
            return redirect('/retrieve')

    return render(request,'updateid.html',{'emp':emp})














