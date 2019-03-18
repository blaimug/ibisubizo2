from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def signedin(request):
    return render(request,'signedin.html')

def problem(request):
    return render(request,'problem.html')

def post(request):
    return render(request,'post.html')

def editpost(request):
    return render(request,'edit-post.html')

def logged(request):
    return render(request,'signedin.html')

def user(request):
    return render(request,'user.html')

def about(request):
    return render(request,'about.html')