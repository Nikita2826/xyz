from django.shortcuts import render,redirect
from .forms import PersonForm
from .models import Person
from django.contrib.auth.decorators import login_required


@login_required(login_url="/a2/lv/")
def add_view(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv")
    return render(request,"app1/add.html",{"form":form})

@login_required(login_url="/a2/lv/")
def show_view(request):
    obj = Person.objects.all()
    return render(request,"app1/show.html",{"person":obj})

def update_view(request,pk):
    obj = Person.objects.get(Pid=pk)
    form = PersonForm(instance=obj)
    if request.method == "POST":
        form = PersonForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/add.html",{"form":form})

def delete_view(request,pk):
    obj = Person.objects.get(Pid=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("/a1/sv/")
    return render(request,"app1/confirn.html",{"obj":obj})