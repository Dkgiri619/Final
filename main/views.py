from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def home(request):
    
    form= ContactForm(request.POST or None)
    if form.is_valid():
        data = request.POST.copy()
        name= data.get("contact_name")
        email= data.get("contact_email")
        phone = data.get("contact_phone")
        comment=data.get("comment")
         
        stuff = [name, email, comment, phone]
        
        listToStr = '\n '.join([str(elem) for elem in stuff])

        send_mail('recieved mail from website', listToStr , 'work4lanceindia@gmail.com' , ['work4lanceindia@gmail.com'], fail_silently=False )
        print(listToStr)

        context= {'form': form}

        return render(request, 'index.html', context)

    else:
        context= {'form': form}
        return render(request, 'index.html', context)



def services(request):
    return render(request, 'services.html')