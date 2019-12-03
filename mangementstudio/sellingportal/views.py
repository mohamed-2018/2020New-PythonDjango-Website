from django.shortcuts import render
from django.http import HttpResponse
from sellingportal import models
from sellingportal import Forms
# Create your views here.
def Index(request):
    context={'name':'mohamed','age':25,'jobs':['eng','dev','lecture']}
    return render(request,'Index.html',context)


    #return HttpResponse('Welcome to index page')
def Student(request):
    students= models.Student.objects.all()
    context ={'students':students}
    return render(request, 'Students.html', context)
    #return HttpResponse('Welcome to Student page ')
def StudentDegree(request,student_id):
    Degrees = models.Degree.objects.filter(student_id=student_id)
    students = models.Student.objects.get(id=student_id)
    msg = ''
    form_data = Forms.DegreeRegister(request.POST or None)
    if form_data.is_valid():
        degree = models.Degree()
        degree.student_Degree= form_data.cleaned_data['student_Degree']
        degree.student_id = students
        degree.save()
        msg = 'data is saved'
    context = {'Degrees': Degrees,'formregister':form_data ,'msg':msg}
    return render(request, 'Degrees.html', context)

def Register(request):
    msg =''
    form_data = Forms.UserRegister(request.POST or None)
    if form_data.is_valid():
        student = models.Student()
        student.First_name = form_data.cleaned_data['First_name']
        student.Last_name = form_data.cleaned_data['Last_name']
        student.age = form_data.cleaned_data['age']
        student.Data_birth = form_data.cleaned_data['Data_birth']
        student.save()
        msg = 'data is saved'

    context = {'formregister':form_data , 'msg':msg}
    return  render(request,'register.html',context)




    #return HttpResponse('Welcome to  degree page your id : '+ student_id)
