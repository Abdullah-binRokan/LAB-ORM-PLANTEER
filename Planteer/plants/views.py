from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant

# Create your views here.
def plants_all_view(request: HttpRequest):
    plants = Plant.objects.all()

    return render(request, "plants/plants_all.html", {"plants": plants})


def plants_detail_view(request: HttpRequest, plant_id):
    try:
        plant = Plant.objects.get(pk = plant_id)
        plants = Plant.objects.all().filter(category = plant.category)[0:3]
    except:
        return redirect("main:home_view")

    return render(request, "plants/plants_detail.html", {"plant": plant, "plants": plants})





def plants_new_view(request: HttpRequest):
    try:
        # Print the data received to help with debugging
        print("Name:", request.POST.get("name"))
        print("Category:", request.POST.get("category"))
        print("About:", request.POST.get("about"))
        print("Is Edible:", request.POST.get("is_edible"))
        print("Used For:", request.POST.get("used_for"))
        print("Image:", request.FILES.get("image"))

        if request.method == "POST":
            plant = Plant(
                name = request.POST["name"],
                category = request.POST["category"],
                about = request.POST["about"],
                is_edible = request.POST["is_edible"] == "True",
                used_for = request.POST["used_for"],
                image = request.FILES["image"],
            )

            plant.save()
            return redirect("main:home_view")
        
    except:
        redirect("main:home_view")

    return render(request, "plants/plants_new.html")


def plants_update_view(request: HttpRequest, plant_id):
    try:
        # get the post by the id
        plant = Plant.objects.get(pk = plant_id)

        # Check if the form was submited by post method
        if request.method == "POST":
            plant.name = request.POST["name"]
            plant.category = request.POST["category"]
            plant.about = request.POST["about"]
            plant.is_edible = request.POST["is_edible"] == "True"
            # check if he updated the image
            if "image" in request.FILES:
                plant.image = request.FILES["image"]
            plant.save()

            return redirect("plants:plants_update_view", plant_id = plant.id)

    except:
        return redirect("main:home_view")

    return render(request, "plants/update.html", {"plant": plant})