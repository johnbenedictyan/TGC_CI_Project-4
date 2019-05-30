from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request,"index.html")

def test_page(request):
    return render(request,"test.html")