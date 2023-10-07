from django.shortcuts import render, HttpResponse
from home.models import  Contact

def home(request):
    context = {'name' : 'Niladree' , 'course' : 'Django'}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    #return HttpResponse("This is my (/contact)")
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        #print(name,email,phone,message)
        contact_instence = Contact(name = name, email = email, phone = phone,  message = message)
        contact_instence.save() 
        print("The data has been written to the Database")
    return render(request, 'contact.html')
