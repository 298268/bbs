from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponseRedirect
from bbs import models
from django.contrib.auth import login,logout,authenticate
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
# Create your views here.


def show(request):
    articles=models.Article.objects.all()
    print(articles)
    return render(request,"bbs/home.html",{"articles":articles})

def forumid(request,id):
    articles=models.Article.objects.filter(category_id=id)


    return render(request,"bbs/index.html",{"articles":articles})

def articleid(request,aid):
    article=models.Article.objects.get(id=aid)
    comments = models.Comment.objects.filter(article_id=article.id)
    return render(request,"bbs/article.html",{"article":article,"comments":comments})
def userlogin(request):
    err=''
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect("/")
        else:
            err="用户名错误或密码错误"
    return render(request,"bbs/login.html",{"err":err})
def userlogout(request):
    logout(request)
    return HttpResponseRedirect("/")
def articlepost(request):
    if request.method=="POST":
        title=request.POST.get("title")
        category=request.POST.get("category")
        categoryID=models.Category.objects.get(name=category).id
        content=request.POST.get("content")
        author=request.user.userprofile.name
        authorID=models.UserProfile.objects.get(name=author).id
        models.Article.objects.create(title=title,category_id=categoryID,content=content,author_id=authorID)


    categories=models.Category.objects.all()
    return render(request, "bbs/articlepost.html", {"categories":categories})
def articlereply(request,aid):
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
    if request.method=="POST":
        print(aid)
        comment=request.POST.get("comment")
        models.Comment.objects.create(article_id=aid,author_id=request.user.userprofile.id,comment=comment)

    return HttpResponseRedirect("/article/"+aid)
def userregister(request):
    err=''
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        email=request.POST['email']
        user=User.objects.filter(username=username)
        if user.exists():
            err="用户名已注册"
            return render(request, "bbs/register.html", {"err": err})
        else:
            new=User.objects.create(username=username,password=make_password(password),email=email)
            new.save()
            newuser=models.UserProfile.objects.create(user=new,name=new.username)
            newuser.save()
            err="注册成功,已登陆"
            login(request, new)
            return render(request,"bbs/register.html",{"err":err})
    return render(request,"bbs/register.html")

