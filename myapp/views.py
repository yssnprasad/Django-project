from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Blog
# Create your views here.

def HomePage(request):
    return render (request,'home.html')

def MainPage(request):
    post=Blog.objects.all()
    return render (request,'main.html',{'post':post})

def AboutusPage(request):
    return render (request,'aboutus.html')

def demo(request):
    return render (request,'demo.html')

def Termscondition(request):
    return render (request,'termscondition.html')

def Disclaimer(request):
    return render (request,'disclaimer.html')

def PrivacyPolicy(request):
    return render (request,'Privacy Policy.html')

def contactus(request):
    return render (request,'contactus.html')

def topice1(request):
    return render (request,'topice1.html')

def topich1(request):
    return render (request,'topich1.html')

def topict1(request):
    return render (request,'topict1.html')

def topice2(request):
    return render (request,'topice2.html')

def topich2(request):
    return render (request,'topich2.html')

def topict2(request):
    return render (request,'topict2.html')

def topice3(request):
    return render (request,'topice3.html')

def topict3(request):
    return render (request,'topict3.html')

def topich3(request):
    return render (request,'topich3.html')


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('main')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')


def CreateBlog(request):
    
    if request.method =='POST':
        title = request.POST['title']
        image = request.FILES.get('image')
        description = request.POST['description']
        author = request.POST['author']
        new_blog = Blog.objects.create(title=title,image=image,description=description,author=author)
        new_blog .save()
        return redirect('main')
    return render(request, 'createblog.html')


def TechnologyInformation(request):
    return render (request,'Technology Information.html')

def Hacking(request):
    return render (request,'Hacking Course.html')

def EarnAway(request):
    return render (request,'Earn Away.html')