from django.shortcuts import render,redirect
from .models import product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import product
from django.contrib.auth.forms import UserCreationForm
@login_required
def home(request):
    return render(request,'index.html')

def enterdetails(request):
    name= request.POST['name']
    price= request.POST['price']
    brand= request.POST['brand']
    description=request.POST['description']
    

    prodobj=product(name=name,price=price,brand=brand,description=description)
    prodobj.save()
    return render(request,'index.html',{"msg":"product added"})


def productinfo(request):
      proddtls=product.objects.all()
      return render(request,"index.html",{'pro':proddtls})


def delproduct(request):
      prodname=request.POST['name']
      proddtls=product.objects.filter(name=prodname)
      proddtls.delete()
      return render(request,'index.html',{"msg":"deleted"})
def updatename(request):
      try:
            oldname=request.POST["oldname"]
            newname=request.POST["newname"]
            prod=product.objects.filter(name=oldname)
            if prod.exists():
                  prod.update(name=newname)
                  return render(request,"index.html",{'msg1':"updated"})
            else:
                return render(request,"index.html",{'msg1':"no records"})
        
      except Exception as e:
            print(e)
            return render(request,"index.html",{'msg1':"not updated"})
    
def loginview(request):
      uname = request.POST['username']
      pwd = request.POST['password']
      user= authenticate(request,username=uname,password=pwd)
      if user is not None:
            login(request,user)
            return redirect('home')
      else:
            return render(request,"login.html",{"msg":"invalid login"})
def logout_view(request):
      logout(request)
      return redirect('login') 

def sign_up(request):
      try:
            form = UserCreationForm(request.POST)
            if request.method =="POST":
                  if form.is_valid():
                        form.save()
                        return redirect('login')
                  
            else:
                  return render(request,'sign_up.html',{'form':userform,'msg':'invalid login'})
      except Exception as e:
            print(e)
            userform=UserCreationForm()
            return render(request,'sign_up.html',{'form': userform})
