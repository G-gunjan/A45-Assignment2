from django.shortcuts import render

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')  
