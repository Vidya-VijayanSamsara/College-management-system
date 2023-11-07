from django.shortcuts import render
from application.models import Admin,Login,Staff,Student
# Create Home page Function
def entry_page(request):
    return render(request,'index.html')

# Go to login or register page of admin Function
def admin_register_login(request):
    return render(request, 'admin_register_login.html')
#admin Registration
def admin_register(request):
    admin_name=request.POST['admin_name']
    admin_username=request.POST['admin_username']
    admin_mail=request.POST['admin_mail']
    admin_pwd=request.POST['admin_pwd']
    data1=Admin(admin_name=admin_name,admin_username=admin_username,admin_mail=admin_mail)
    data1.save()
    data2=Login(username=admin_username,pwd=admin_pwd,status=1)
    data2.save()
    return render(request,'admin_register_login.html')

#update personal details of admin
def admin_update(request):
    username=request.post['admin_username']
    data=Admin.objects.get(admin_username=username)
    data.admin_name=request.post['admin_name']
    data.admin_username=request.post['admin_username']
    data.admin_mail=request.post['admin_mail']
    data.admin_qualification=request.post['admin_qualification']
    data.admin_post=request.post['admin_post']
    data.admin_yoj=request.post['admin_yoj']
    data.admin_experience=request.post['admin_experience']
    data.admin_place=request.post['admin_place']
    data.save()
    return render(request,'adminmain.html')
# Go to login or register page of staff Function
def staff_register_login(request):
    return render(request, 'staff_register_login.html')
#Staff Registration
def staff_register(request):
    staff_name=request.POST['staff_name']
    staff_username=request.POST['staff_username']
    staff_mail=request.POST['staff_mail']
    staff_pwd=request.POST['staff_pwd']
    data1=Staff(staff_name=staff_name,staff_username=staff_username,staff_mail=staff_mail)
    data1.save()
    data2=Login(username=staff_name,pwd=staff_pwd,status=2)
    data2.save()
    return render(request,'staff_register_login.html')
# Go to login or register page of student Function
def student_register_login(request):
    return render(request, 'student_register_login.html')
#Staff Registration
def student_register(request):
    student_name=request.POST['student_name']
    student_username=request.POST['student_username']
    student_mail=request.POST['student_mail']
    student_pwd=request.POST['student_pwd']
    data1=Student(student_name=student_name,student_username=student_username,student_mail=student_mail)
    data1.save()
    data2=Login(username=student_username,pwd=student_pwd,status=3)
    data2.save()
    return render(request,'student_register_login.html')
#login function
def login(request):
    try:
        username=request.POST['username']
        password=request.POST['password']
        m=Login.objects.get(username=username,pwd=password)
        if m.status==1:
            request.session[username] = m.username
            d=Admin.objects.get(admin_username=m.username)
            return render(request,'adminmain.html',{'d':d})
        if m.status==2:
            request.session[username] = m.username
            d= Staff.objects.get(staff_username=m.username)
            return render(request, 'staffmain.html', {'d': d})
        if m.status==3:
            request.session[username] = m.username
            d = Student.objects.get(student_username=m.username)
            return render(request, 'studentmain.html', {'d': d})
        return render(request, "index.html")
    except:
        return render(request,"index.html")
def home(request):
    return render(request,'index.html')