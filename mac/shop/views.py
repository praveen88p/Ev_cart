from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import product ,Contact,Orders
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from math import ceil
import logging
logger = logging.getLogger(__name__)

def index(request):
    # products=product.objects.all()
    
    # n=len(products)
    # nSlides= n//4 + ceil((n/4)-(n//4))

    allprods = []
    catprods=product.objects.values('category', 'id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n=len(prod)
        nSlides= n//4 + ceil((n/4)-(n//4))
        allprods.append([prod, range(1,nSlides),nSlides])
    # params = {'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    # allprods= [[products,range(1,nSlides), nSlides],
    #           [products,range(1,nSlides), nSlides]]
    params={'allprods':allprods}          
    return render(request,"shop/index.html",params)

def about(request):
    return render(request,"shop/about.html")
    

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request,"shop/tracker.html")


def search(request):
    return render(request,"shop/search.html")

def productview(request,myid):
    products=product.objects.filter(id=myid)
    
    return render(request,"shop/productview.html",{'productview':products[0]})
  

    
def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'shop/checkout.html')
    # if request.method=="POST":
    #     name = request.POST.get('name', '')
    #     email = request.POST.get('email', '')
    #     phone = request.POST.get('phone', '')
    #     address = request.POST.get('address', '') + " " + request.POST.get('address2', '')
    #     city = request.POST.get('city', '')
    #     state = request.POST.get('state', '')
    #     zip_code = request.POST.get('zip_code', '')
    #     order = Oders(name=name, email=email, phone=phone, address=address,city=city,state=state, zip_code=zip_code)
    #     order.save()
    #     # thank=True
    #     # id=order.order_id
    #     # return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})

    # return render(request,"shop/checkout.html")

        

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            auth_login(request,user)
            return redirect('shop')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'shop/login.html')

def logout(request):
    logout(request)
    return redirect('login')
  

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render (request,'shop/signup.html')
