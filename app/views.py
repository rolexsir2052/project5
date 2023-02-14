from django.shortcuts import render,redirect
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def home(request):
    B=Client.objects.all()
    d={'B':B}
    return render(request,'home.html',d)
def create_data(request):
    
    if request.method=='POST':
        N=request.POST['name']
        E=request.POST['email']
        P=request.POST['number']
        
        data=Client.objects.get_or_create(Name=N,Email=E,Phone=P)[0]
        data.save()
        return redirect('homes')
    return render(request,'home.html',{'O':O})
def delete_data(request,id):
    C=Client.objects.get(id=id)
    C.delete()
    return redirect('homes')  
def edit_data(request,id):
    if request.method=='POST':
        N=request.POST['name']
        E=request.POST['email']
        P=request.POST['number'] 
        X=Client.objects.get(id=id)
        X.name=N
        X.email=E
        X.phone=P
        X.save()
        return redirect('homes')
    else:
        V=Client.objects.get(id=id)
        d={'V':V}
        return render(request,'edit.html',d)
def data(request):
    X=ClientForm_User()
    d={'X':X}
    if request.method=='POST':
        D=ClientForm_User(request.POST)
        if D.is_valid():
            D.save()
        return HttpResponse('yes i inserted data')
    return render(request,'edit.html',d)
    