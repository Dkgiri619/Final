from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    if request.method=='POST':
        message = request.POST[ 'Contact_Number']
        email = request.POST['email']
        send_mail(
            'Website_contact',
            message,
            settings.EMAIL_HOST_USER,
            email,
            fail_silently= False
        )
        return render(request, 'index.html')

    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')