from django.shortcuts import redirect, render
from .forms import blog_form, signupform
from .models import post_class
# Create your views here.

def home(request):
    return render(request, "home.html")

def write_post(request):
    if request.method == "POST" :
        form = blog_form(request.POST or None,request.FILES or None )
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            return redirect(read_posts)
    else:
        form = blog_form()
    return render(request,'write.html',{'form':form})   

def read_posts(request):
    read = post_class.objects.all()
    return render(request, "posts.html", {'read': read})

def signup(request):
    if request.method=='POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home)
    else:
        form = signupform()
    return render(request,'registration/signup.html',{'form':form})


def view_post(request, id):
    entry = post_class.objects.get(id=id)
    return render(request, "post_view.html", {'i':entry})

def update_post(request, id):
    entry = post_class.objects.get(id=id)
    form = blog_form(request.POST or None,request.FILES or None, instance=entry )
    if request.method == "POST" :
        if form.is_valid():
            form.save()
            return redirect(read_posts)

    return render(request, "update.html", {'i' : form})

def delete_post(request, id):
    deleted = post_class.objects.get(id=id)
    d = deleted
    deleted.delete()
    return render(request, "on_delete.html", {'i' : d})