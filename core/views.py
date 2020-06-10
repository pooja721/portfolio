from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def home(request):
    context={'home':'active'}
    return render(request,'core/home.html',context)




def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():

            your_name = form.cleaned_data['your_name']
            your_email = form.cleaned_data['your_email']

            your_message = form.cleaned_data['your_message']
            try:
                send_mail(your_name, your_message, your_email, ['raip8173@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "core/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Thank you for contact us. We will contact you soon..')




