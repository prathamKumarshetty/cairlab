from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages
from math import ceil
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


# gpt for faculty
from .models import Faculty

from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def AIML(request):
    faculties = Faculty.objects.all()
    n = len(faculties)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides + 1), 'faculty': faculties}
    return render(request, "AIML.html", params)

def CLOUD(request):
    return render(request,"CLOUD.html")
def DATASCIENCE(request):
    return render(request,"DATASCIENCE.html")
def OTHER(request):
    return render(request,"OTHER.html")
def HPC(request):
    return render(request,"HPC.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        # Check if all required fields are filled
        if name and email and phone and desc:
            # Create and save the Contact object
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            messages.success(request, "Your Message Has Been Sent.")
        else:
            messages.success(request, "Your Message Has  not been Been Sent.")

        
    
    return render(request, "contact.html")



#gpt
def FacultyLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login succesful.")
            return redirect('faculty_dashboard')  # Redirect to a home or another desired page after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'FacultyLogin.html')

# gpt
def faculty_dashboard(request):
    # Add any logic or context data needed for the faculty dashboard page
    return render(request, 'faculty_dashboard.html')


def research_domains(request):
    faculties = Faculty.objects.all()
    return render(request, 'AIML.html', {'faculties': faculties})


def aiml_view(request):
    faculties = [
        # Replace this with your actual data
        {'name': 'Faculty 1', 'domain': 'AI', 'description': 'Expert in AI', 'link': '#', 'image': {'url': 'url-to-image-1'}},
        {'name': 'Faculty 2', 'domain': 'ML', 'description': 'Expert in ML', 'link': '#', 'image': {'url': 'url-to-image-2'}}
    ]
    return render(request, 'AIML.html', {'faculties': faculties})