from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.

def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            
            # Enviar el Email
            email = EmailMessage(
                "Mensaje de contacto recibido",
                f"Mensaje enviado por {name} <{email}>:\n\n{message}",
                   email,
                    ["f048b6e945f009@inbox.mailtrap.io"],
                    reply_to=[email],
            )
            try:
                email.send()
                #esta todo ok
                return redirect(reverse('contact')+'?ok')
            except:
                #ha habido un error en el retorno a error
                return redirect(reverse('contact')+'?error')
            
    return render(request, 'contact/contact.html', {'form':contact_form})