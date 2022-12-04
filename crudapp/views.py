from django.shortcuts import render,redirect
from crudapp.models import Employee
# Create your views here.
def index(request):
    data=Employee.objects.all().values()
    param={'members':data}
    return render(request,'index.html',param)

def back(request):
    optype=request.POST['optype']
    if optype=='add':
        nm=request.POST['nm']
        add=request.POST['add']
        e=Employee(nm=nm,add=add)
        e.save()
    return redirect('/index/')

def deleteData(request,id):
        data=Employee.objects.get(id=id)
        data.delete()
        return redirect('/index/')

def update(request,id):
    data=Employee.objects.get(id=id)
    param={'data':data}
    return render(request,'update.html',param)

def updaterecord(request, id):
    unm = request.POST['unm']
    uadd = request.POST['uadd']
    e = Employee.objects.get(id=id)
    e.nm = unm
    e.add = uadd
    e.save()
    return redirect('/index/')

    
