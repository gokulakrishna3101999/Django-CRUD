from django.shortcuts import redirect, render
from .models import Student
from .forms import StudentForm

# Create your views here.
def home(req):
    data = Student.objects.all().order_by('register_no');
    print(data)
    return render(req,"read.html",{"student":data})

def create(req):
    if req.method == "POST":
        form = StudentForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return redirect('create')
    else:
        form = StudentForm()
    return render(req,"create.html",{"form":form})

def update(req,id):
    studentToBeUpdated = Student.objects.get(id=id)
    print(studentToBeUpdated)
    if req.method == "POST":
        form = StudentForm(req.POST,instance=studentToBeUpdated)
        if form.is_valid():
            form.save()
            return redirect('/')
        return redirect('/')
    else:
        form = StudentForm()
        
    return render(req,'update.html',{"form":form})

def delete(req,id):
    studentToBeDeleted  = Student.objects.get(id=id)
    if studentToBeDeleted.delete():
        return redirect('read');
    return render(req,'read.html',) 