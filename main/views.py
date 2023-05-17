from django.shortcuts import render, redirect
from .models import Category, Base, Button_1, Button_2, Button_3, Button_4, Footer, Contack


# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        Contack.objects.create(name = name, email = email, message = message)
        return redirect("index")

    category1 = Category.objects.all()[0]
    category2 = Category.objects.all()[1]
    category3 = Category.objects.all()[2]
    category4 = Category.objects.all()[3]
    button_1 = Button_1.objects.all()[0]
    button_2 = Button_2.objects.all()[0]
    button_3 = Button_3.objects.all()
    button_4 = Button_4.objects.all()[0]
    footer = Footer.objects.all()[0]

    base = Base.objects.all()[0]
    return render(request, 'main/index.html', context={
        "category1": category1,
        "category2": category2,
        "category3": category3,
        "category4": category4,
        "button_1": button_1,
        "button_2": button_2,
        "button_3": button_3,
        "button_4": button_4,
        "footer": footer,

        "base": base,


    })