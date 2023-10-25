from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team
def demo(request):
    obj=Place.objects.all()
    o1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'r1':o1})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})
#
# def contact(request):
#     return HttpResponse("I am contact")
