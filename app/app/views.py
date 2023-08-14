from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from . models import PB, User, Hospital, Bed
# Create your views here.
def home(request):
    return render(request, 'home.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password)
        
        if user:
            request.session['username'] = username
            beds=Bed.objects.all()
            return render(request, 'beds.html', {'beds': beds})
        else:
            return render(request, 'userlogin.html', {'error': 'Invalid Username or Password'})
    else:
        return render(request, 'userlogin.html')

def hospitallogin(request):
    if request.method == 'POST':
        request.session['hospitalcode'] = request.POST['hospitalcode']
        hospitalcode = request.POST['hospitalcode']
        password = request.POST['password']
        hospital = Hospital.objects.filter(hospitalcode=hospitalcode, password=password)
        if hospital:
            return redirect('hospitalbedmanagement')
        else:
            return render(request, 'hospitallogin.html', {'error': 'Invalid Hospital Code or Password'})
    else:
        return render(request, 'hospitallogin.html')

def usersignup(request):

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        username = request.POST['username']
        password = request.POST['password']
        user  = User.objects.create(name=name, age=age, username=username, password=password)
        user.save()
        return redirect('userlogin')
    else:
        return render(request, 'usersignup.html')  

def hospitalsignup(request):
    if request.method == 'POST':
        hospitalname = request.POST['hospitalname']
        hospitalcode = request.POST['hospitalcode']
        password = request.POST['password']
        hospital  = Hospital.objects.create(hospitalname=hospitalname, hospitalcode=hospitalcode, password=password)
        hospital.save()
        hospitalbed = Bed.objects.create(hospitalcode=hospital, bedtype1=0, bedtype2=0, bedtype3=0)
        hospitalbed.save()
        return redirect('hospitallogin')
    else:
        return render(request, 'hospitalsignup.html')


def hospitalbedmanagement(request):
    if request.method == 'POST':
        hospitalcode = request.POST['hospitalcode']
        bedtype1 = request.POST.get('bedtype1')
        bedtype2 = request.POST.get('bedtype2')
        bedtype3 = request.POST.get('bedtype3')
        print(bedtype1)
        hospital = Hospital.objects.filter(hospitalcode=hospitalcode).first()
        if hospital:
            bed = Bed.objects.filter(hospitalcode=hospital).first()
            print(bed.bedtype1)
            bed.bedtype1 = bedtype1
            bed.bedtype2 = bedtype2
            bed.bedtype3 = bedtype3
            bed.save()
            print(bed.bedtype1)
            return render(request, 'hospitalloginportal.html')
        else:
            return render(request, 'hospitalloginportal.html', {'error': 'Invalid Hospital Code'})
    else:
        return render(request, 'hospitalloginportal.html')

def bedstatus(request):
    if request.method == 'POST':
        hospitalcode = request.POST['hospitalcode']
        hospital = Hospital.objects.filter(hospitalcode=hospitalcode).first()
        if hospital:
            return HttpResponseRedirect(reverse('hospitalloginportal', args = (hospitalcode)))
        else:
            return render(request, 'beds.html', {'error': 'Invalid Hospital Code'})
    else:
        beds = Bed.objects.all()
        return render(request, 'beds.html', {'beds': beds})

def bookbed(request, hospitalcode):
    if request.method == 'POST':
        user=User.objects.filter(username=request.session['username']).first()
        bedtype = request.POST.get('bedtype')
        print(bedtype)
        hospital = Hospital.objects.filter(hospitalcode=hospitalcode).first()
        print(hospital)
        if hospital:
            bed = Bed.objects.filter(hospitalcode=hospital).first()
            if bedtype == 'ICU BED' and bed.bedtype1 > 0:
                bed.bedtype1 -= 1
                bed.save()
                pb = PB.objects.create(user=user, hospitalcode=hospital, bedtype="ICU Bed")
                pb.save()
                return redirect('bedstatus')
            elif bedtype == 'NORMAL BED' and bed.bedtype2 > 0:
                bed.bedtype2 -= 1
                bed.save()
                pb = PB.objects.create(user=user, hospitalcode=hospital, bedtype="Normal Bed")
                pb.save()
                return redirect('bedstatus')
            elif bedtype == 'VENTILATOR BED' and bed.bedtype3 > 0:
                bed.bedtype3 -= 1
                bed.save()
                pb = PB.objects.create(user=user, hospitalcode=hospital, bedtype="Ventilator Bed")
                pb.save()
                return redirect('bedstatus')
            else:
                return render(request, 'hospitalloginportal.html', {'error': 'No Beds Available'})
        else:
            return render(request, 'hospitalloginportal.html', {'error': 'Invalid Hospital Code'})
    else:
        return render(request, 'bookbed.html', {'hospitalcode': hospitalcode})  

def patient(request):

    user=User.objects.filter(username=request.session['username']).first()
    pb = PB.objects.filter(user=user).all()
    return render(request, 'patient.html', {'user': user, 'pb': pb})

def logout(request):
    del request.session['username']
    return redirect('home')

def hlogout(request):
    del request.session['hospitalcode']
    return redirect('home')