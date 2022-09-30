from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from crudapp.form import UserForm
from crudapp.models import User
# Create your views here.

def insert(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid:
            try:
                form.save()
                return redirect('/show')
            except:
                pass

    form = UserForm()
    return render(request, 'index.html',{'form':form})

# showing data from database on show.html
def show(request):
    users = User.objects.all()
    return render(request, 'show.html',{'users':users})

#deleting user from database with its id
def delete(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/show")

def update(request,id):
    user = User.objects.get(id=id)
    return render(request, 'update.html',{'user':user})

def updated(request,id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST,instance=user)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'update.html',{'user':user})