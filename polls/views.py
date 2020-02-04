from django.shortcuts import render

# Create your views here.
def pollView(request):
    return render(request,"index.html");