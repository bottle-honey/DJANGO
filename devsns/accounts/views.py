from django.shortcuts import redirect, render
from django.contrib import auth
# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    return render(request, 'register.html')