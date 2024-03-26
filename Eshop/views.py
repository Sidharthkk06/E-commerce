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
        product = Product.objects.get(id=pid)
        return render(request,"Eshop/product_detail.html",{'product':product})
    

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
    

class AddToCart(View):
    def get(self, request, *args, **kwargs):
        item_id = kwargs.get('pid')
        product = Product.objects.get(id=item_id)
        if request.user.is_authenticated:
            Cart.objects.create(item=product, user=request.user)
            messages.success(request, "added sucessfully")
            return redirect("cart_detail")
        else:
            messages.error(request, "Please Login First to add items to the cart")
            return redirect("register")
    

class CartDelete(View):
    def get(self, request,*args,**kwargs):
        item_id = kwargs.get("pid")

        # Delete the cart item
        Cart.objects.get(id=item_id).delete()
        messages.success(request, "Item removed from cart sucessfully")
        # Fetch updated cart items after deletion
        updated_cart_items = Cart.objects.filter(user=request.user)

        # Render the cart template with updated cart items
        return render(request, "Eshop/cart.html",{"item":updated_cart_items})
    

class CartDetail(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            item = Cart.objects.filter(user=request.user)
            return render(request,"Eshop/cart.html",{"item":item})
        else:
            return redirect('register')  # Redirect to the register page if the user is not authenticated