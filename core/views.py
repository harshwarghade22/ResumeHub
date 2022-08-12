from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout
from .models import Skill,Academic,Referee,Profile,User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password



def index(request):
    return render(request, 'core/index.html')


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
    return render(request, 'core/login.html')


@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')


def createCv(request):
    return render(request, 'core/create_cv.html')



def saveSkill(request):
    if request.method == 'POST':
        s_name = request.POST.getlist('s_name[]')
        s_level = request.POST.getlist('s_level[]')
        
        if(len(s_name) == 1):
            a = Skill(s_name = s_name[0], s_level=s_level[0], cv_id=1)
            a.save()
            return JsonResponse({'status':1})
        else:
            for x,y in zip(s_level,s_name):
                a = Skill(s_name=x, s_level=y, cv_id=1)
                a.save()
            return JsonResponse({'status':1})
    return JsonResponse({'status':0})
                



def saveEducation(request):
    if request.method == 'POST':
        name = request.POST.getlist('name[]')
        year = request.POST.getlist('year[]')
        award = request.POST.getlist('award[]')

        if(len(name) == 1):
            a = Academic(a_institution = name[0], a_year=year[0], a_award=award[0], cv_id=1)
            a.save()
            return JsonResponse({'status':1})
        else:
            for x,y,z in zip(name,year,award):
                a = Academic(a_institution=x, a_year=y, a_award=z, cv_id=1)
                a.save()
            return JsonResponse({'status':1})
    return JsonResponse({'status':0})




def saveReferee(request):
    if request.method == 'POST':
        name = request.POST.getlist('name[]')
        phone = request.POST.getlist('phone[]')
        email = request.POST.getlist('email[]')

        if(len(name) == 1):
            a = Referee(r_name = name[0], r_email=email[0], r_phone=phone[0], cv_id=1)
            a.save()
            return JsonResponse({'status':1})
        else:
            for x,y,z in zip(name,phone,email):
                a = Referee(r_name=x, r_phone=y, r_email=z, cv_id=1)
                a.save()
            return JsonResponse({'status':1})
    return JsonResponse({'status':0})





def uploadProfile(request):
    fname = request.POST.get('fname')
    mname = request.POST.get('mname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    gender = request.POST.get('gender')
    bio = request.POST.get('bio')
    dob = request.POST.get('dob')
    occupation = request.POST.get('occupation')
    country = request.POST.get('country')
    region = request.POST.get('region')
    file = request.FILES.get('file')

    fss = FileSystemStorage()
    filename = fss.save(file.name, file)
    url = fss.url(filename)
    print(file.name)

    p = Profile(fname=fname, mname=mname, lname=lname, email=email, bio=bio, dob=dob, gender=gender, occupation=occupation, country=country, region=region, avator=file,phone=phone,cv_id=1)
    p.save()

    return JsonResponse({'status':1})




def registerView(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password = make_password(password)

        check_user = User.objects.filter(username=username).count()
        check_email = User.objects.filter(email=email).count()

        if(check_user > 0):
            messages.error(request, 'Username is already taken')
            return redirect('reg-form')
        elif(check_email > 0):
            messages.error(request, 'Email is already taken')
            return redirect('reg-form')
        else:
            User.objects.create(username=username, email=email, password=password)
            messages.success(request, 'Account created successfully, Please Sign In')
            return redirect('reg-form')
    else:
        return render(request, 'core/register.html')        



def logoutView(request):
    logout(request)
    return redirect('index')



def viewPDF(request, id=None):
    user_profile = Profile.objects.filter(cv_id=id).values()

    context = {'user_profile':user_profile}
    return render(request, 'core/pdf_template.html', context)



        