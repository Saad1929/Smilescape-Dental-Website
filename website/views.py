from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError

# Create your views here.

def home(request):

    if request.method == "POST":
        name = request.POST['your-name']
        phone = request.POST['your-phone']
        email = request.POST['your-email']
        address = request.POST['your-address']
        schedule = request.POST['your-scheldule']
        time = request.POST['your-time']

        message_start = "A customer wishes to make a booking, please approve or disapprove.\n"
        message_details = "\nName: " + name + "\nPhone: " + phone + "\nEmail: " + email + "\nAddress: " + address + "\nSchedule: " + schedule + "\nTime: " + time 
        final_message = message_start + message_details

        try:
            send_mail("Contact Smilescape - New Booking Request",
                  final_message,
                  email,
                  ["saaddjango7@gmail.com"],
                  fail_silently=False)
        except BadHeaderError:
            pass
        return render(request, 'home.html', {'name' : name})
    else:
        return render(request, 'home.html', {})

def contact(request):

    if request.method == "POST":
        message_name = request.POST['message-name'] #message-name is the form name in contact page
        message_email = request.POST['message-email'] #message-email is the form name in contact page
        message = request.POST['message'] #message is the form name

        #If User Has Typed a message, Email With what they wrote
        message_to_send = "Message From: " + message_email + "\n\n" + message
        try:
            send_mail("Contact Smilescape - New Message",
                  message_to_send,
                  message_email,
                  ["saaddjango7@gmail.com"],
                  fail_silently=False)
        except BadHeaderError:
            pass
        return render(request, 'contact.html', {'message_name' : message_name})
    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def service(request):
    return render(request, 'service.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def blog(request):
    return render(request, 'blog.html', {})
