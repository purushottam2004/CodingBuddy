from django.shortcuts import render

# Create your views here.

def checklogincredentials(request):
    if(request.method == 'POST'):
        from .models import student
        contact = request.POST['contact']
        password = request.POST['password']
        students = student.objects.all()
        studentfilter = students.filter(contact = contact , password=password)
        if(len(studentfilter) == 1):
            from .models import test
            from .models import ans
            tests = test.objects.all()
            pending = tests.filter(for_student = studentfilter[0], issolved = False)
            solved = tests.filter(for_student = studentfilter[0], issolved = True)
            downloads = ans.objects.all().filter(for_student = studentfilter[0])
            return render(request, 'home.html', {'student':studentfilter[0],'pending' : pending, 'solved' : solved, 'downloads' : downloads, 'message' :'Valid Credentials'})
        else:
            return render(request, 'login.html', {'student' : False, 'message':'Invalid Credentials'})
    else:
        return render(request, 'login.html', {'student' : False, 'message':'Some Error Occured'})

def signuprequest(request):
    if(request.method == 'POST'):
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']
        if(password != confirm_password):
            return render(request, 'signup.html', {'student' : False, 'message':'Password and Confirm Password do not match'})
        email = request.POST['email']
        name = request.POST['name']
        contact = request.POST['contact']
        from .models import student
        students = student.objects.all()
        studentfilter = students.filter(contact=contact)
        if(len(studentfilter) ==1):
            return render(request, 'signup.html', {'student' : False, 'message':'Contact Number already exists'})
        newstudent  = student( name=name, email=email, contact=contact, password=password)
        newstudent.save()
        return render(request, 'login.html', {'student' : False, 'message':'Signup Successful'})

    else:
        return render(request, 'signup.html', {'student' : False, 'message':'Some Error Occured'})

def login(request):
    return render(request, 'login.html', {'student' : False, 'message':'Initial Login Page'})

def process_form(request):
    if(request.method == 'POST'):
        from .models import test
        from .models import ans
        from .models import student
        contact = request.POST['contact']
        question_name = request.POST['question_name']
        question_zip = request.FILES['zip_file']
        studentfor = student.objects.all().get(contact = contact)
        newtest = test(question_name = question_name, question_zip = question_zip, for_student = studentfor, issolved = False)
        newtest.save()
        tests = test.objects.all()
        students = student.objects.all()
        studentfilter = students.filter(contact = contact)
        pending = tests.filter(for_student = studentfilter[0], issolved = False)
        solved = tests.filter(for_student = studentfilter[0], issolved = True)
        downloads = ans.objects.all().filter(for_student = studentfilter[0])
        return render(request, 'home.html', {'student':student,'message' :'Question Uploaded Successfully', 'pending' : pending, 'solved' : solved, 'downloads' : downloads})
    else:
        return render(request, 'home.html', {'student':student,'message' :'Some Error Occured'})
    
def signuppage(request):
    return render(request, 'signup.html', {'student' : False, 'message':'Initial Signup Page'})