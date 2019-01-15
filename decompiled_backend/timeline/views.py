from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
def index(request):
    if request.user.is_authenticated:
        return render(request,'timeline.html')
    else:
        a=redirect('login')
        return a





from django.core.mail import send_mail

if form.is_valid():
    author=form.cleaned_data['']
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']
    sender = form.cleaned_data['sender']
    cc_myself = form.cleaned_data['cc_myself']

    recipients = ['info@example.com']
    if cc_myself:
        recipients.append(sender)

    send_mail(subject, message, sender, recipients)
    return HttpResponseRedirect('/thanks/')
