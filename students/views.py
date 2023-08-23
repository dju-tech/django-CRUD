from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import StudentForm

def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})

def view_student(request, id):
    students = Students.objects.get(pk = id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']
            
            
            new_student = Student(
                student_number=new_student_number,
                first_name=new_first_name,
                last_name=new_last_name,
                email = new_email,
                field_of_study=new_field_of_study,
                gpa = new_gpa
            )
            
            new_student.save()
            
            return redirect('/')
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {'form': form})

def update(request, student_id):
    print(id)
    context = {}
    student = get_object_or_404(Student, id=int(student_id))
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')

    # url = reverse('update', kwargs={'student_id' : student.id })

    context = {
        'form' : StudentForm(instance=student),
        'student_id' : student.id
        # 'url' : url
    }
        
    return render(request, 'students/update.html', context)

def delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('/')