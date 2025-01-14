from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
           login_form = AuthenticationForm() 
        
    else:
        login_form = AuthenticationForm()
    
    return render(request, 'login.html', {'login_form': login_form})  

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('cars_list')
    else:
            user_form = UserCreationForm()

    return render(request, 'register.html', {'user_form': user_form}) 