from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {})

def contact(request):

    if request.method == "POST":
        message_name = request.POST['message-name'] #message-name is the form name in contact page
        message_email = request.POST['message-email'] #message-email is the form name in contact page
        message = request.POST['message'] #message is the form name

        #If User Has Typed a message, Email With what they wrote
        

        return render(request, 'contact.html', {'message_name' : message_name})
    else:
        return render(request, 'contact.html', {})
