from winreg import REG_DWORD_BIG_ENDIAN
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from .forms import profileupdateform
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if(request.method == 'POST'):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Account Created.')
            return redirect('login')

    else:
        form=RegisterForm()
    return render(request, 'accounts/register.html', {'form':form})        
@login_required
def profile(request):
    return render(request,'accounts/profile.html')

def profileupdate(request):
    if (request.method == 'POST'):
        pform = profileupdateform(request.POST, request.FILES, instance=request.user.profile)
        if pform.is_valid():
            pform.save()
            return redirect('profile')

    else:
        pform= profileupdateform(instance = request.user.profile)
            
    
    return render (request,'accounts/profileupdate.html',{'pform':pform})