from datetime import datetime
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
from shree.serializers import UserSerializer, UserSerializer
from shree.models import Contact, Leave, Review, User
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/getUsers/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array Users'
        },

        {
            'Endpoint': '/getUser/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an one array User'
        },

        {
            'Endpoint': '/createUser/',
            'method': 'POST',
            'body': {"first_name","last_name","department","User_id","mobile","address","email","username","password"},
            'description': 'Returns an one array createUser'
        },
        

        # {
        #     "body": {
        #             "first_name": "Manish",
        #             "last_name": "Rao",
        #             "department": "Research",
        #             "User_id": "1588",
        #             "mobile": "9450016188",
        #             "address": "Varanasi",
        #             "email": "raomanish@gmail.com",
        #             "username": "raomanish",
        #             "password": "Manish@321"
        #         }
        # }

    ]
    return Response(routes)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getUser(request, username):
    if User.objects.filter(username = username).exists():
        user = User.objects.get(username = username)
        serializer = UserSerializer(User, many = False)
        return Response(serializer.data)
    else:
        messages = [{"message": "User does not exists."}]
        return Response(messages)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def createUser(request):
    data = request.data
    user = User.objects.create_user(first_name=data["first_name"], last_name=data["last_name"], email=data["email"], username=data["username"], password=data["password"])
    
    user = User(user = user, name = data["first_name"]+' '+data["last_name"], department = data["department"], user_id = data["User_id"], mobile = data["mobile"], email = data["email"], username = data["username"], address = data["address"])
    user.save()
    serializer = UserSerializer(user, many = False)
    return Response(serializer.data)


def signOut(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')


def signIn(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        
        try:
            user=User.objects.get(username = loginusername, password = loginpassword)
        except:
            user=authenticate(username = loginusername, password = loginpassword)
        if user is not None:
            auth_login(request, user)
            messages.info(request, "You have successfully logged in.")
            return redirect("home")
        else:
            messages.warning(request, "Invalid credentials! Please try again.")
            return redirect('home')

    return HttpResponse("404- Not found.")


def SignUp(request):
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
        username=request.POST['username']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if pass1 == pass2:
            # Create the user
            myuser = User.objects.create_user(type, fname, lname, eid, role, department, branch, mobile, email, address, username, pass1)
            myuser.save()
            messages.success(request, " Your User has been successfully created")
            return redirect('home')
        else:
            messages.success(request, " Your User Passwords are Miss-Matched")
            return redirect('home')

    else:
        return HttpResponse("404 - Not found")

    
def rate1(request, username):
    tuser = User.objects.filter(username=username).first()
    if Review.objects.filter(fuser=request.user, tuser=tuser).exists():
        review = Review.objects.get(fuser=request.user, tuser=tuser)
        review.rating = 1
        review.save()
    else:
        rating = Review(fuser=request.user, tuser=tuser, rating=1)
        rating.save()
    return redirect('user',username)

def rate2(request, username):
    tuser = User.objects.filter(username=username).first()
    if Review.objects.filter(fuser=request.user, tuser=tuser).exists():
        review = Review.objects.get(fuser=request.user, tuser=tuser)
        review.rating = 2
        review.save()
    else:
        rating = Review(fuser=request.user, tuser=tuser, rating=2)
        rating.save()
    return redirect('user',username)

def rate3(request, username):
    tuser = User.objects.filter(username=username).first()
    print(tuser)
    if Review.objects.filter(fuser=request.user, tuser=tuser).exists():
        review = Review.objects.get(fuser=request.user, tuser=tuser)
        review.rating = 3
        review.save()
    else:
        rating = Review(fuser=request.user, tuser=tuser, rating=3)
        rating.save()
    return redirect('user',username)

def rate4(request, username):
    tuser = User.objects.filter(username=username).first()
    if Review.objects.filter(fuser=request.user, tuser=tuser).exists():
        review = Review.objects.get(fuser=request.user, tuser=tuser)
        review.rating = 4
        review.save()
    else:
        rating = Review(fuser=request.user, tuser=tuser, rating=4)
        rating.save()
    return redirect('user',username)

def rate5(request, username):
    tuser = User.objects.filter(username=username).first()
    if Review.objects.filter(fuser=request.user, tuser=tuser).exists():
        review = Review.objects.get(fuser=request.user, tuser=tuser)
        review.rating = 5
        review.save()
    else:
        rating = Review(fuser=request.user, tuser=tuser, rating=5)
        rating.save()
    return redirect('user',username)
    
@login_required
def user(request, username):
    tuser=User.objects.get(username=username)
    if Review.objects.filter(fuser=request.user, tuser=tuser).exists():
        review=Review.objects.get(fuser=request.user, tuser=tuser)
    else:
        review = None
    context={'user':tuser, 'review':review}
    return render(request,'shree/user.html', context)

@login_required
def users(request):
    users = User.objects.all()
    reviews=Review.objects.all()
    for u in users:
        n=0
        a=0
        for r in reviews:
           if u.id == r.tuser.id:
               n += 1
               a += r.rating
               ae = User.objects.get(id = r.tuser.id)
               ae.arating = a/n
               ae.save()
    
    return render(request, 'shree/users.html', {'users': users, 'reviews':reviews})

@login_required
def profile(request, username):
    if Review.objects.filter(fuser=request.user,tuser=request.user).exists():
        review=Review.objects.get(tuser=request.user, fuser=request.user)
    else:
        review = None
    return render(request, 'shree/profile.html', {'review':review})


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
def leave(request,username):
    user = User.objects.get(username= request.user)
    if Leave.objects.filter(user=request.user).exists():
        leave = Leave.objects.filter(user=request.user).last()
    else:
        leave = None
    if leave != None:
        if leave.status == 'Approved':
            user.ldays = 24 - leave.days
            user.save()
        # elif leave.status == 'Rejected':
        #     User.ldays += leave.days
        #     User.save()

    if request.method == 'POST':
        df = request.POST['df']
        dt = request.POST['dt']
        type = request.POST['type']
        
        # Parse the dates from strings into datetime objects
        date1 = datetime.strptime(f'{df}', "%Y-%m-%d")
        date2 = datetime.strptime(f'{dt}', "%Y-%m-%d")
        # Calculate the difference between the two dates
        difference = relativedelta.relativedelta(date2, date1)
        days = difference.days
        if user.type == "HOD":
            leave = Leave(user=request.user, df=df, dt=dt, type=type, days=days, status="Pending", hod_approved=True)
        elif user.type == "E":
            leave = Leave(user=request.user, df=df, dt=dt, type=type, days=days, status="Pending")
        leave.save()
        return redirect('leave',user)

    return render(request, 'shree/leave.html',{'user':user, 'leave':leave})


@login_required
def leaves(request):
    leaves = Leave.objects.all()
    return render(request, 'shree/leaves.html', {'leaves': leaves})


@login_required
def hod_verify(request, request_id):
    # Verify the holiday request by HoD
    leave = Leave.objects.get(id=request_id)
    leave.hod_approved = True
    leave.save()
    return redirect('leaves')


@login_required
def ceo_verify(request, request_id):
    # Verify the holiday request by CEO
    leave = Leave.objects.get(id=request_id)
    leave.ceo_approved = True
    leave.approved = True
    leave.status = "Approved"
    leave.save()
    return redirect('leaves')

@login_required
def hod_rejection(request, request_id):
    # Verify the holiday request by CEO
    leave = Leave.objects.get(id=request_id)
    leave.hod_approved = False
    leave.approved = False
    leave.status = "Rejected"
    leave.save()
    return redirect('leaves')

@login_required
def ceo_rejection(request, request_id):
    # Verify the holiday request by CEO
    leave = Leave.objects.get(id=request_id)
    leave.ceo_approved = False
    leave.approved = False
    leave.status = "Rejected"
    leave.save()
    return redirect('leaves')

# @user_passes_test(lambda u: u.is_superuser)
# def leaves(request):
#     leaves = Leave.objects.all()
#     return render(request, 'shree/leaves.html', {'leaves': leaves})



