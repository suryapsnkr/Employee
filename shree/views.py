from datetime import datetime, date
from dateutil import relativedelta
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth  import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import JsonResponse
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from shree.serializers import EmployeeSerializer, EmployeeSerializer
from shree.models import Contact, Leave, Review, Employee
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def getRoutes(request):
#     routes = [
#         {
#             'Endpoint': '/getemps/',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns an array Employees'
#         },

#         {
#             'Endpoint': '/getemp/',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns an one array Employee'
#         },

#         {
#             'Endpoint': '/createEmployee/',
#             'method': 'POST',
#             'body': {"first_name","last_name","department","eid","mobile","address","email","eid","password"},
#             'description': 'Returns an one array createEmployee'
#         },
        

#         # {
#         #     "body": {
#         #             "first_name": "Manish",
#         #             "last_name": "Rao",
#         #             "department": "Research",
#         #             "eid": "1588",
#         #             "mobile": "9450016188",
#         #             "address": "Varanasi",
#         #             "email": "raomanish@gmail.com",
#         #             "eid": "raomanish",
#         #             "password": "Manish@321"
#         #         }
#         # }

#     ]
#     return Response(routes)


# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def getemps(request):
#     employees = Employee.objects.all()
#     serializer = EmployeeSerializer(employees, many = True)
#     return Response(serializer.data)


# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def getemp(request, eid):
#     if employee.objects.filter(eid = eid).exists():
#         employee = Employee.objects.get(eid = eid)
#         serializer = EmployeeSerializer(Employee, many = False)
#         return Response(serializer.data)
#     else:
#         messages = [{"message": "Employee does not exists."}]
#         return Response(messages)


# @api_view(['POST'])
# @permission_classes((permissions.AllowAny,))
# def createEmployee(request):
#     data = request.data
#     employee = Employee.objects.create_Employee(fname=data["fname"], lname=data["lname"], email=data["email"], eid=data["eid"], password=data["password"])
    
#     employee = Employee(employee = employee, name = data["fname"]+' '+data["lname"], department = data["department"], eid = data["eid"], mobile = data["mobile"], email = data["email"], eid = data["eid"], address = data["address"])
#     Employee.save()
#     serializer = EmployeeSerializer(Employee, many = False)
#     return Response(serializer.data)


def signOut(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')


def signIn(request):
    if request.method == "POST":
        # Get the post parameters
        logineid = request.POST['logineid']
        loginpassword = request.POST['loginpassword']
        
        try:
            employee=Employee.objects.get(eid = logineid, password = loginpassword)
        except:
            employee=authenticate(eid = logineid, password = loginpassword)
        if employee is not None:
            auth_login(request, employee)
            messages.info(request, "You have successfully logged in.")
            return redirect("home")
        else:
            messages.warning(request, "Invalid credentials! Please try again.")
            return redirect('home')

    return HttpResponse("404- Not found.")


def signUp(request):
    if request.method=="POST":
        # Get the post parameters
        type=request.POST['type']
        fname=request.POST['fname']
        lname=request.POST['lname']
        eid=request.POST['eid']
        role=request.POST['role']
        department=request.POST['department']
        branch=request.POST['branch']
        mobile=request.POST['mobile']
        email=request.POST['email']
        address=request.POST['address']
        pass1=request.POST['pswd1']
        pass2=request.POST['pswd2']


        if pass1 == pass2:
            if Employee.objects.filter(eid=eid).exists():
                messages.warning(request, " Your Employee has been already exists")
                return redirect('home')
            else:
                # Create the Employee
                emp = Employee.objects.create_user(eid=eid, password=pass1)
                emp.type=type
                emp.fname=fname
                emp.lname=lname
                emp.role=role
                emp.department=department
                emp.branch=branch
                emp.mobile=mobile
                emp.email=email
                emp.address=address
                emp.save()
                messages.success(request, " Your Employee has been successfully created")
                return redirect('home')
        else:
            messages.success(request, " Your Employee Passwords are Miss-Matched")
            return redirect('home')

    else:
        return HttpResponse("404 - Not found")

    
def rate1(request, eid):
    temp = Employee.objects.filter(eid=eid).first()
    if Review.objects.filter(femp=request.user, temp=temp).exists():
        review = Review.objects.get(femp=request.user, temp=temp)
        review.rating = 1
        review.save()
    else:
        rating = Review(femp=request.user, temp=temp, rating=1)
        rating.save()
    return redirect('employee',eid)

def rate2(request, eid):
    temp = Employee.objects.filter(eid=eid).first()
    if Review.objects.filter(femp=request.user, temp=temp).exists():
        review = Review.objects.get(femp=request.user, temp=temp)
        review.rating = 2
        review.save()
    else:
        rating = Review(femp=request.user, temp=temp, rating=2)
        rating.save()
    return redirect('employee',eid)

def rate3(request, eid):
    temp = Employee.objects.filter(eid=eid).first()
    print(temp)
    if Review.objects.filter(femp=request.user, temp=temp).exists():
        review = Review.objects.get(femp=request.user, temp=temp)
        review.rating = 3
        review.save()
    else:
        rating = Review(femp=request.user, temp=temp, rating=3)
        rating.save()
    return redirect('employee',eid)

def rate4(request, eid):
    temp = Employee.objects.filter(eid=eid).first()
    if Review.objects.filter(femp=request.user, temp=temp).exists():
        review = Review.objects.get(femp=request.user, temp=temp)
        review.rating = 4
        review.save()
    else:
        rating = Review(femp=request.user, temp=temp, rating=4)
        rating.save()
    return redirect('employee',eid)

def rate5(request, eid):
    temp = Employee.objects.filter(eid=eid).first()
    if Review.objects.filter(femp=request.user, temp=temp).exists():
        review = Review.objects.get(femp=request.user, temp=temp)
        review.rating = 5
        review.save()
    else:
        rating = Review(femp=request.user, temp=temp, rating=5)
        rating.save()
    return redirect('employee',eid)
    
@login_required
def employee(request, eid):
    temp=Employee.objects.get(eid=eid)
    if Review.objects.filter(femp=request.user, temp=temp).exists():
        review=Review.objects.get(femp=request.user, temp=temp)
    else:
        review = None
    context={'temp':temp, 'review':review}
    return render(request,'shree/employee.html', context)

@login_required
def employees(request):
    emps = Employee.objects.all()
    reviews=Review.objects.all()
    for e in emps:
        n=0
        a=0
        for r in reviews:
           if e.id == r.temp.id:
               n += 1
               a += r.rating
               ae = Employee.objects.get(id = r.temp.id)
               ae.arating = a/n
               ae.save()
    if request.method=="POST":
        eid=request.POST['eid']
        if Employee.objects.filter(eid = eid).exists():
            f = Employee.objects.get(eid = eid)
        else:
            f=''
    else:
        f=''
    return render(request, 'shree/employees.html', {'emps': emps, 'reviews':reviews,'f':f})


def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        content=request.POST['content']
        # check for error
        contact=Contact(name=name, email=email, content=content)
        contact.save()
        messages.info(request, "Your message has been successfully sent")
        # send_mail
    #     send_mail(
    #     'SunCoder',
    #     'Thanks for contact us.',
    #     'suryapsnkr@gmail.com',
    #     [email],
    #     fail_silently=False,
    # )
        # EmailMultiAlternatives
        subject='Testing Mail'
        form_email='suryapsnkr@gmail.com'
        msg='<p><b>Welcome'+' '+f'{name}'+',</b><br>'+'<i>Thanks for contact to us.</i>'
        to=email
        msg=EmailMultiAlternatives(subject,msg,form_email,[to])
        msg.content_subtype='html'
        msg.send()
        return redirect('contact')
    return render(request, 'shree/contact.html')


def about(request, time=datetime.now().strftime('%B')):
    now = datetime.now()
    # get current time
    time = now.strftime('%I:%M %p')
    return render(request, 'shree/about.html',{'time': time})


def home(request):
    return render(request, 'shree/home.html')

def hod(request):
    return render(request, 'shree/hod.html')

def ceo(request):
    return render(request, 'shree/ceo.html')


@login_required
def leave(request,eid):
    emp = Employee.objects.get(eid=request.user)
    if date.today().day == 1:
        emp.ldays += 2
    if Leave.objects.filter(emp=request.user).exists():
        leaves = Leave.objects.filter(emp=request.user).all()
    else:
        leaves = None
        emp.ldays = 2
        emp.save()

    if request.method == 'POST':
        df = request.POST['df']
        dt = request.POST['dt']
        type = request.POST['type']
        
        # Parse the dates from strings into datetime objects
        date1 = datetime.strptime(f'{df}', "%Y-%m-%d")
        date2 = datetime.strptime(f'{dt}', "%Y-%m-%d")
        # Calculate the difference between the two dates
        difference = relativedelta.relativedelta(date2, date1)
        days = difference.days+1
        if emp.type == "HOD":
            leave = Leave(emp=request.user, df=df, dt=dt, type=type, days=days, status="Pending", hod_approved=True)
        elif emp.type == "E":
            leave = Leave(emp=request.user, df=df, dt=dt, type=type, days=days, status="Pending")
        leave.save()
        return redirect('leave',eid)

    return render(request, 'shree/leave.html',{'emp':emp, 'leaves':leaves})


@login_required
def leaves(request):
    leaves = Leave.objects.all()
    return render(request, 'shree/leaves.html', {'leaves': leaves})


@login_required
def hod_verify(request, rid):
    # Verify the holiday request by HOD
    leave = Leave.objects.get(id=rid)
    leave.hod_approved = True
    leave.save()
    return redirect('leaves')


@login_required
def ceo_verify(request, rid):
    # Verify the holiday request by CEO
    leave = Leave.objects.get(id=rid)
    leave.ceo_approved = True
    leave.approved = True
    leave.status = "Approved"
    leave.save()
    emp = Employee.objects.get(eid=leave.emp)
    emp.ldays -= leave.days
    emp.save()
    return redirect('leaves')

@login_required
def hod_rejection(request, rid):
    # Verify the holiday request by HOD
    leave = Leave.objects.get(id=rid)
    leave.hod_approved = False
    leave.approved = False
    leave.status = "Rejected"
    leave.save()
    return redirect('leaves')

@login_required
def ceo_rejection(request, rid):
    # Verify the holiday request by CEO
    leave = Leave.objects.get(id=rid)
    leave.ceo_approved = False
    leave.approved = False
    leave.status = "Rejected"
    leave.save()
    return redirect('leaves')



