import email
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def edit_page(request):
    return render(request, "edit.html")


def subscribe_page(request):
    return render(request, "subscribe.html")


def dar_page(request):
    return render(request, "dar.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        city = request.POST.get('city')

        query = Student(name=name,
                        email=email,
                        age=age,
                        gender=gender,
                        country=country,
                        city=city)
        query.save()
        return redirect("/")

    return render(request, 'index.html')


def update_Data(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        country = request.POST.get("country")
        city = request.POST.get("city")

        update_info = S.objects.get(id=id)
        update_info.name = name
        update_info.email = email
        update_info.age = age
        update_info.gender = gender
        update_info.country = country
        update_info.city = city
        update_info.save()

        messages.success(request, 'Updated successfully')
        return redirect("/")

    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request, 'edit.html', context)
