from django.shortcuts import render, redirect, HttpResponse,get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Product
# Create your views here.
from .forms import SignUpForm
def index(request):
    context = {

    }
    return render(request,'product/index.html',context)

def productlist(request):
    product_list = Product.objects.all()
    context = {
        'products':product_list,
    }
    return render(request,'product/productlist.html',context)

def productdetail(request,id):
    product = get_object_or_404(Product,pk=id)

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('productlisting')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})