from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm
from django.contrib  import messages
from datetime import *
from django.utils import timezone
from django.db.models import Q

# Create your views here.

def home(request):
    searched = request.GET.get('searched')

    if searched:
        students = Student.objects.filter(full_name__icontains=searched, is_delete=False)
    else:
        students = Student.objects.filter(is_delete=False).order_by('id')
        
    delete_student = Student.objects.filter(is_delete=True)
    
    return render(request, 'app/index.html', {'students': students, 'delete_student': delete_student})

# create data
def create(request):
    if request.method == 'POST':
        roll_number = request.POST.get('roll_number')
        full_name = request.POST.get('full_name')
        faculty = request.POST.get('faculty')
        semester = request.POST.get('semester')
        reason = request.POST.get('reason')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        leave_type = request.POST.get('leave_type')
        guardian_contact = request.POST.get('guardian_contact')
        student_contact = request.POST.get('student_contact')
        student_email = request.POST.get('student_email')
        
        Student.objects.create(
            roll_number = roll_number,
            full_name = full_name,
            faculty = faculty,
            semester = semester,
            reason = reason,
            start_date = start_date,
            end_date = end_date,
            leave_type = leave_type,
            guardian_contact = guardian_contact,
            student_contact = student_contact,
            student_email = student_email,
        )
        messages.success(request, "Your leave application is submited! ")
        return redirect('create')
    return render(request, 'app/form.html')

# Update or edit data
def update(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.roll_number = request.POST.get('roll_number')
        student.full_name = request.POST.get('full_name')
        student.faculty = request.POST.get('faculty')
        student.semester = request.POST.get('semester')
        student.reason = request.POST.get('reason')
        student.start_date = request.POST.get('start_date')
        student.end_date = request.POST.get('end_date')
        student.leave_type = request.POST.get('leave_type')
        student.guardian_contact = request.POST.get('guardian_contact')
        student.student_contact = request.POST.get('student_contact')
        student.student_email = request.POST.get('student_email')
        student.save()
        messages.success(request, "Your leave applicaion is updated! ")
        return redirect('home')
    return render(request, 'app/form.html', {'students': student})

# Recycle Bin
def recycle(request):
    student = Student.objects.filter(is_delete=True)
    threshold = timezone.now() - timedelta(days=30)
    expired = Student.objects.filter(is_delete=True, deleted_time__lt=threshold)
    
    count = expired.count()
    if count > 0:
        student.delete()
    else:
        print("Empty")
    return render(request, 'app/recycle.html', {'students': student})

# Soft Delete data
def soft_delete(request, id):
    student = Student.objects.get(id=id)
    student.is_delete = True
    student.deleted_time = timezone.now()
    student.save()
    return redirect('home')

def soft_clear_all(request):
    Student.objects.filter(is_delete=False).update(is_delete=True, deleted_time=timezone.now())
    return redirect('home') 

# hard delete data
def delete_hard(request, id):
    Student.objects.filter(id=id).delete()
    messages.success(request, "Permanantly deleted!")
    return redirect('recycle')

def clear_all(request):
    Student.objects.filter(is_delete=True).delete()
    messages.success(request, "Permanantly deleted!")
    return redirect('recycle')

# restore data
def restore(request, id):
    student = Student.objects.get(id=id)
    student.is_delete = False
    student.save()
    return redirect('recycle')

def restore_all(request):
    Student.objects.filter(is_delete=True).update(is_delete=False)
    messages.success(request, "Restore all data!")
    return redirect('recycle')

# About Page
def about(request):
    return render(request, 'app/about.html')

# Contact Page
def contact(request):
    if request.method == "POST":
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            messages.success(request, "Your contact application is submited! ")
            return redirect('contact')
    else:
        contact = ContactForm()
    data = Contact.objects.all()
    return render(request, 'app/contact.html', {'contact': contact, 'data': data})

def view_contact(request):
    contact = Contact.objects.filter(is_delete=False)
    del_contact = Contact.objects.filter(is_delete=True)
    
    return render(request, 'app/contact_view.html', {'contacts': contact, 'delete_data': del_contact})

def recycle_contact(request):
    contact = Contact.objects.filter(is_delete=True)
    threshold = timezone.now() - timedelta(days=30)
    exp = Contact.objects.filter(is_delete=True, deleted_time__lt=threshold)
    
    count_exp = exp.count()
    if count_exp > 0:
        contact.delete()
    else:
        print('Empty')
    
    return render(request, 'app/recycle_contact.html', {'contacts': contact})

def del_soft_contact(request, id):
    data = Contact.objects.get(id=id)
    data.is_delete = True
    data.deleted_time = timezone.now()
    data.save()
    return redirect('view_contact')

def soft_clear_all_contact(request):
    Contact.objects.filter(is_delete=True).update(is_delete=False, deleted_time=timezone.now)
    messages.success(request, "Cleared all data. ")
    return redirect('view_contact')

def del_contact(request,id):
    Contact.objects.get(id=id).delete()
    messages.success(request, "Permanantly deleted successful.  ")
    return redirect('recycle_contact')
    
def clear_contact(request):
    Contact.objects.filter(is_delete=True).delete()
    messages.success(request, "Permanantly deleted all data successfully.  ")
    return redirect('recycle_contact')

def retore_contact(request, id):
    data = Contact.objects.get(id=id)
    data.is_delete = False
    data.save()
    return redirect('recycle_contact')

def restore_all_contact(request):
    Contact.objects.filter(is_delete=True).update(is_delete=False)
    messages.success(request, "Restore all data successfully. ")
    return redirect('recycle_contact')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    