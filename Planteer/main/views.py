from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Message
from plants.models import Plant

# Create your views here.
def home_view(request: HttpRequest):
    plants = Plant.objects.all()[1:4]

    return render(request, "main/index.html", {"plants": plants})


def contact_view(request: HttpRequest):
    try:
        if request.method == "POST":
            message = Message(
                first_name = request.POST["first_name"],
                last_name = request.POST["last_name"],
                email = request.POST["email"],
                message = request.POST["message"]
            )

            message.save()
            return redirect("main:contact_messages_view")
        
    except:
        redirect("main:home_view")

    return render(request, "main/contact.html")


def contact_messages_view(request: HttpRequest):
    messages = Message.objects.all()

    return render(request, "main/contact_messages.html", {"messages": messages})