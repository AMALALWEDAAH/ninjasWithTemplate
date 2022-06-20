from django.shortcuts import render ,redirect
from .models import dojos ,ninjas

# Create your views here.
def index(request):
    context ={
        "dojos": dojos.objects.all()
    }
    return render(request,"index.html",context)

def add_dojo(request):
    dojos.objects.create(
        name=request.POST["name"],
        city=request.POST["city"],
        state=request.POST["state"],
    )
    return redirect("/")

def add_ninja(request):
    selector = dojos.objects.get(id=request.POST["dojo_id"])
    
    ninjas.objects.create(
        first_name = request.POST["first_name"],
        last_name = request.POST["last_name"],
        dojo = selector,
        )
    return redirect("/")