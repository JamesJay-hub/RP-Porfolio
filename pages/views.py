from django.shortcuts import render



def home_view(request):
    return render(request, "pages/home.html")

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def custom_500_view(request):
    return render(request, '500.html', status=500)

def home(request):
    return render(request, "pages/home.html", {})