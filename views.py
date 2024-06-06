from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import User

def hello(request):
    return HttpResponse("Hello, World!")

def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def new_user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
      
        role = request.POST.get('role')
         # Check for duplicate email
        if User.objects.filter(email=email).exists():
            return HttpResponse("Duplicate email found. Please enter a unique email.")

    

            
        User.objects.create(name=name, email=email, role=role)
        return redirect('users')
    return render(request, 'new_user.html')

def user_detail(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'user_detail.html', {'user': user})

# def delete_user(request, id):
#     user = User.objects.get(id=id)
#     user.delete()
#     return redirect('users')

