from django.shortcuts import render , redirect
from .models import *
from .forms import *
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

# Create your views here.
@login_required
def view_home(request):
    return render(request, 'reqtracker/dashboard.html')

#View user dashboard
@login_required
def view_dash_user(request):

    requests = MainRequest.objects.filter(user=request.user)
    # req_p = MainRequest.objects.filter(status="Pending",user=request.user)
    # req_c = MainRequest.objects.filter(status="Completed",user=request.user))
    # req_i = MainRequest.objects.filter(status="In Progress",user=request.user))
    
    labels = ['Pending','In Progress','Completed']
    labels1 = ['Civil','MEP']
    queryset = MainRequest.objects.filter(status='Pending',user=request.user)
    queryset1 = MainRequest.objects.filter(status='In Progress',user=request.user)
    queryset2 = MainRequest.objects.filter(status='Completed',user=request.user)
    queryset3 = MainRequest.objects.filter(Maintenance_Type='Civil',user=request.user).count()
    queryset4 = MainRequest.objects.filter(Maintenance_Type='MEP',user=request.user).count()
    data = [queryset.count(),queryset1.count(),queryset2.count()]
    data1 = [queryset3,queryset4]
    return render(request, 'reqtracker/dashboard-user.html',{
        'requests':requests,
        'labels':labels,
        'data':data,
        'labels1':labels1,
        'data1':data1,
        'queryset':queryset,
        'queryset1':queryset1,
        'queryset2':queryset2
        })

#View admin dashboard
@login_required
def view_dash_admin(request):
    labels = ['Pending','In Progress','Completed']
    labels1 = ['Civil','MEP']
    labels2 = ['Painting','Carpentry','Masonry']
    labels3 = ['Mechanical','Electrical','Plumbing']
    queryset = MainRequest.objects.filter(status='Pending').count()
    queryset1 = MainRequest.objects.filter(status='In Progress').count()
    queryset2 = MainRequest.objects.filter(status='Completed').count()
    queryset3 = MainRequest.objects.filter(Maintenance_Type='Civil').count()
    queryset4 = MainRequest.objects.filter(Maintenance_Type='MEP').count()
    queryset5 = MainRequest.objects.filter(Nature_Civil='Painting').count()
    queryset6 = MainRequest.objects.filter(Nature_Civil='Carpentry').count()
    queryset7 = MainRequest.objects.filter(Nature_Civil='Masonry').count()
    queryset8 = MainRequest.objects.filter(Nature_MEP='Mechanical - Pump, motors, HVAC').count()
    queryset9 = MainRequest.objects.filter(Nature_MEP='Electrical - lighting, switch').count()
    queryset10 = MainRequest.objects.filter(Nature_MEP='Plumbing').count()
    data = [queryset,queryset1,queryset2]
    data1 = [queryset3,queryset4]
    data2 = [queryset5,queryset6,queryset7]
    data3 = [queryset8,queryset9,queryset10]
    
    requests = MainRequest.objects.all()
    todays_req = MainRequest.objects.filter(date_created=datetime.date.today())
    req_pending = MainRequest.objects.filter(status="Pending")
    req_completed = MainRequest.objects.filter(status="Completed")
    req_in = MainRequest.objects.filter(status="In Progress")
    context = {
        'requests':requests,
        'tr':todays_req,
        'labels':labels,
        'data':data,
        'labels1':labels1,
        'data1':data1,
        'labels2':labels2,
        'data2':data2,
        'labels3':labels3,
        'data3':data3,
        'req_pending':req_pending,
        'req_completed':req_completed,
        'req_in':req_in
    }
    return render(request, 'reqtracker/dashboard-admin.html',context)

#View supervisor dashboard
@login_required
def view_dash_super(request):
    labels = ['Pending','In Progress','Completed']
    if request.user.username == "SPRC1":
        req = MainRequest.objects.filter(Maintenance_Type='Civil',Zone__in=['1','2','3','4','5'])
        queryset = MainRequest.objects.filter(Maintenance_Type='Civil',Zone__in=['1','2','3','4','5'],status='Pending')
        queryset1 = MainRequest.objects.filter(Maintenance_Type='Civil',Zone__in=['1','2','3','4','5'],status='In Progress')
        queryset2 = MainRequest.objects.filter(Maintenance_Type='Civil',Zone__in=['1','2','3','4','5'],status='Completed')
        z1 = MainRequest.objects.filter(Maintenance_Type='Civil', Zone='1').count()
        z2 = MainRequest.objects.filter(Maintenance_Type='Civil', Zone='2').count()
        z3 = MainRequest.objects.filter(Maintenance_Type='Civil', Zone='3').count()
        z4 = MainRequest.objects.filter(Maintenance_Type='Civil', Zone='4').count()
        z5 = MainRequest.objects.filter(Maintenance_Type='Civil', Zone='5').count()
        data = [queryset.count(),queryset1.count(),queryset2.count()]
        data2 = [z1,z2,z3,z4,z5]
        t = ['Civil']
        labels2 = ["Zone 01", "Zone 02", "Zone 03",'Zone 04','Zone 05']
        return render(request,'reqtracker/dashboard-super.html',{
            'req':req,
            'labels':labels,
            'data':data,
            'data2':data2,
            'labels2':labels2,
            't':t,
            'queryset':queryset,
            'queryset1':queryset1,
            'queryset2':queryset2
            })
    elif request.user.username == "SPRC2":
        req = MainRequest.objects.filter(Maintenance_Type='Civil',Zone__in=['6','7','8','9','10'])
        queryset = MainRequest.objects.filter(Maintenance_Type='Civil',Zone__in=['6','7','8','9','10'],status='Pending')
        queryset1 = MainRequest.objects.filter(Maintenance_Type='Civil',Zone__in=['6','7','8','9','10'],status='In Progress')
        queryset2 = MainRequest.objects.filter(Maintenance_Type='Civil',Zone__in=['6','7','8','9','10'],status='Completed')
        z6 = MainRequest.objects.filter(Maintenance_Type='Civil', Zone='6').count()
        z7 = MainRequest.objects.filter(Maintenance_Type='Civil', Zone='7').count()
        z8 = MainRequest.objects.filter(Maintenance_Type='Civil', Zone='8').count()
        z9 = MainRequest.objects.filter(Maintenance_Type='Civil', Zone='9').count()
        z10 = MainRequest.objects.filter(Maintenance_Type='Civil', Zone='10').count()
        data = [queryset.count(),queryset1.count(),queryset2.count()]
        data2 = [z6,z7,z8,z9,z10]
        t = ['Civil']
        labels2 = ["Zone 06", "Zone 07", "Zone 08",'Zone 09','Zone 10']
        return render(request,'reqtracker/dashboard-super.html',{
            'req':req,
            'labels':labels,
            'data':data,
            'data2':data2,
            'labels2':labels2,
            't':t,
            'queryset':queryset,
            'queryset1':queryset1,
            'queryset2':queryset2
            })
    elif request.user.username == "SPRMEP1":
        req = MainRequest.objects.filter(Maintenance_Type='MEP',Zone__in=['1','2','3','4','5'])
        queryset = MainRequest.objects.filter(Maintenance_Type='MEP',Zone__in=['1','2','3','4','5'],status='Pending')
        queryset1 = MainRequest.objects.filter(Maintenance_Type='MEP',Zone__in=['1','2','3','4','5'],status='In Progress')
        queryset2 = MainRequest.objects.filter(Maintenance_Type='MEP',Zone__in=['1','2','3','4','5'],status='Completed')
        data = [queryset.count(),queryset1.count(),queryset2.count()]
        z1 = MainRequest.objects.filter(Maintenance_Type='MEP', Zone='1').count()
        z2 = MainRequest.objects.filter(Maintenance_Type='MEP', Zone='2').count()
        z3 = MainRequest.objects.filter(Maintenance_Type='MEP', Zone='3').count()
        z4 = MainRequest.objects.filter(Maintenance_Type='MEP', Zone='4').count()
        z5 = MainRequest.objects.filter(Maintenance_Type='MEP', Zone='5').count()
        data2 = [z1,z2,z3,z4,z5]
        t=['MEP']
        labels2 = ["Zone 01", "Zone 02", "Zone 03",'Zone 04','Zone 05']
        return render(request,'reqtracker/dashboard-super.html',{
            'req':req,
            'labels':labels,
            'data':data,
            'data2':data2,
            'labels2':labels2,
            't':t,
            'queryset':queryset,
            'queryset1':queryset1,
            'queryset2':queryset2
            })
    elif request.user.username == "SPRMEP2":
        req = MainRequest.objects.filter(Maintenance_Type='MEP',Zone__in=['6','7','8','9','10'])
        queryset = MainRequest.objects.filter(Maintenance_Type='MEP',Zone__in=['6','7','8','9','10'],status='Pending')
        queryset1 = MainRequest.objects.filter(Maintenance_Type='MEP',Zone__in=['6','7','8','9','10'],status='In Progress')
        queryset2 = MainRequest.objects.filter(Maintenance_Type='MEP',Zone__in=['6','7','8','9','10'],status='Completed')
        z6 = MainRequest.objects.filter(Maintenance_Type='MEP', Zone='6').count()
        z7 = MainRequest.objects.filter(Maintenance_Type='MEP', Zone='7').count()
        z8 = MainRequest.objects.filter(Maintenance_Type='MEP', Zone='8').count()
        z9 = MainRequest.objects.filter(Maintenance_Type='MEP', Zone='9').count()
        z10 = MainRequest.objects.filter(Maintenance_Type='MEP', Zone='10').count()
        data = [queryset.count(),queryset1.count(),queryset2.count()]
        data2 = [z6,z7,z8,z9,z10]
        t=['MEP']
        labels2 = ["Zone 06", "Zone 07", "Zone 08",'Zone 09','Zone 10']
        return render(request,'reqtracker/dashboard-super.html',{
            'req':req,
            'labels':labels,
            'data':data,
            'data2':data2,
            'labels2':labels2,
            't':t,
            'queryset':queryset,
            'queryset1':queryset1,
            'queryset2':queryset2         
            })

#view estimation report
def view_estimation(request,r):
    form = CompletionForm
    reque = MainRequest.objects.filter(Request_Number=r)
    req = Completion.objects.filter(mr=r)
    if request.method == 'POST':
        form = CompletionForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            #return redirect('/estimation_report/')
    context = {'form':form,'req':req,'reque':reque}
    return render(request,"reqtracker/estimation_report.html",context) 

def view_completion_form(request,r):
    form = CompletionForm
    req = MainRequest.objects.filter(Request_Number=r)
    requ = Completion.objects.filter(mr=r)
    if request.method == 'POST':
        form = CompletionForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
    context = {'form':form,'req':req,'requ':requ}
    return render(request,"reqtracker/completion_form.html",context)

# To view requests in user dashboard
@login_required
def view_request(request, pk_r):
    requ = MainRequest.objects.get(id=pk_r)
    context = {'requ':requ}
    
    return render(request,'reqtracker/view_request.html',context)

def view_request_admin(request,pk_r):
    req = MainRequest.objects.get(id=pk_r)
    # u = users.objects.get(id=pk_r)
    # req = u.mainrequest_set.all()
    # count = u.mainrequest_set.all().count()
    context = {'req':req}
    return render(request, 'reqtracker/view_req_admin.html',context)

#For viewing pending requests
def view_pending(request):
    reqq = MainRequest.objects.filter(status="Pending")
    return render(request,'reqtracker/dashboard-admin.html',{'reqq':reqq})

#For viewing completed requests
def view_completed(request):
    reqq = MainRequest.objects.filter(status="Completed")
    return render(request,'reqtracker/dashboard-admin.html',{'reqq':reqq})

#For viewing in progress requests
def view_inprogress(request):
    reqq = MainRequest.objects.filter(status="In Progress")
    return render(request,'reqtracker/dashboard-admin.html',{'reqq':reqq})

def create_request(request):
    form = MainRequestForm
    if request.method == 'POST':
        print('Printing ',request.POST)
        form = MainRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form.clean()
            return HttpResponseRedirect('/dashboard-user/')
    context = {'form':form}
    return render(request,'reqtracker/order_form.html',context)

#Update the request from admin dashboard
def update_req_admin(request, pk):
    req = MainRequest.objects.get(id=pk)
    form = MainRequestFormAdmin(instance=req)
    if request.method == 'POST':
        #print('Printing ',request.POST)
        form = MainRequestFormAdmin(request.POST, request.FILES, instance=req)
        if form.is_valid():
            form.save()
            return redirect('/dashboard-admin/')

    context = {'form':form}
    return render(request,'reqtracker/order_form.html',context)

#Update the request from user dashboard
def update_req_user(request, pk):
    req = MainRequest.objects.get(id=pk)
    form = MainRequestForm(instance=req)
    if request.method == 'POST':
        #print('Printing ',request.POST)
        form = MainRequestForm(request.POST, instance=req)
        if form.is_valid():
            form.save()
            return redirect('/dashboard-user/')

    context = {'form':form}
    return render(request,'reqtracker/order_form.html',context)

def update_status(request,pk):
    req = MainRequest.objects.get(id=pk)
    form = StatusUpdateForm(instance=req)
    if request.method == 'POST':
        #print('Printing ',request.POST)
        form = StatusUpdateForm(request.POST, instance=req)
        if form.is_valid():
            form.save()
            return redirect('/dashboard-super/')

    context = {'form':form}
    return render(request,'reqtracker/status_update.html',context)

def update_estimate(request,pk):
    req = Completion.objects.get(id=pk)
    form = CompletionForm(instance=req)
    if request.method == 'POST':
        form = CompletionForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            #messages.info(request, "Updated Successfully" )
            return redirect('/dashboard-super/')
            #return redirect(f'/{req.mr}/estimation_report/')
    context = {'form':form,'req':req}
    return render(request,'reqtracker/est_form.html',context)

def delete_estimate(request,pk):
    req = Completion.objects.get(id=pk)
    req.delete()
    messages.info(request, "Deleted Successfully" )
    return redirect(request.META['HTTP_REFERER'])

#Delete the request
def del_req(request,pk):
    req = MainRequest.objects.get(id=pk)
    req.delete()
    messages.info(request, "Deleted Successfully" )
    if request.user.username in ['SPRC1','SPRC2','SPRMEP1','SPRMEP2']:
        return redirect('/dashboard-super/')
    elif request.user.username == 'admin':
        return redirect('/dashboard-admin/')
    else:
        return redirect('/dashboard-user/')
    
#Register
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			#login(request, user)
			messages.info(request, "Registration successful." )
			return redirect("/login/")
		messages.info(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

# Login 
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                if request.user.username in ['SPRC1','SPRC2','SPRMEP1','SPRMEP2']:
                    return redirect('/dashboard-super/')
                elif request.user.username == 'admin':
                    return redirect('/dashboard-admin/')
                else:
                    return redirect('/dashboard-user/')
            else:
                messages.info(request,"Invalid username or password.")
        else:
            messages.info(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form":form})

#Logout
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/login/")