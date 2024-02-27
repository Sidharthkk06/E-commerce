from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView
from Eshop.models import Category, Product, Cart
from django.contrib.auth.models import User
from Eshop.forms import RegisterForm, SignInForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class Home(ListView):
    model = Category
    template_name = "Eshop/index.html"
    context_object_name = "categories"


class CategoryDetail(CreateView):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("cd")
        data = Product.objects.filter(category_id = id)
        cname = Category.objects.get(id=id)
        return render(request,"Eshop/category_detail.html",{"data" : data, "cname" : cname})
    

class ProductDetail(View):
    def get(self, request, *args, **kwargs):
        pid = kwargs.get('pid')
        data = Product.objects.get(id=pid)
        return render(request,"Eshop/product_detail.html",{'data':data})
    

class RegisterView(CreateView):
    template_name = "Eshop/register.html"
    form_class = RegisterForm
    model = User
    success_url = reverse_lazy("login")


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, "Eshop/signin.html", {"form" : form})
    
    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user_obj = authenticate(request, username=username, password=password)
            if user_obj:
                login(request,user_obj)
                return redirect("home")
            else:
                return redirect("register")
            

class SignOutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("home")
    

class AddtoCartView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pid')
        data = Product.objects.get(id=id)
        Cart.objects.create(item=data, user=request.user)
        messages.success(request, "added sucessfully")
        return redirect("home")
    

class CartDelete(View):
    def get(self, request,*args,**kwargs):
        id = kwargs.get("pid")
        Cart.objects.get(id=id).delete()
        return redirect("home")
    

class CartDetail(View):
    def get(self, request, *args, **kwargs):
        data = Cart.objects.filter(user=request.user)
        return render(request,"Eshop/cart.html",{"data":data})