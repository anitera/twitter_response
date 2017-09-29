from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from cart.forms import CartAddProductForm
from django.views.decorators.http import require_POST
from django.template import RequestContext
from .models import Registrate
from .forms import RegistrateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages

# Create your views here.

#from .models import Category, Product, Certificate, Increment

# РЎС‚СЂР°РЅРёС†Р° СЃ С‚РѕРІР°СЂР°РјРё
def Teglist(request, category_slug=None):

    return render(request, 'index.html')

def Logout(request,category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	certificates = Certificate.objects.all()
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	logout(request)


	return redirect("shop:ProductList")



# РЎС‚СЂР°РЅРёС†Р° С‚РѕРІР°СЂР°
def ProductDetail(request, id, slug):
    counter = Increment()
    products = Product.objects.all
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,'shop/product/detail.html',
                             {'product': product, 'counter': counter, 'products': products,
                              'cart_product_form': cart_product_form})

def CertificateDetail(request, id, slug):
    certificate = get_object_or_404(Certificate, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request,'shop/product/certificate.html',
                             {'certificate': certificate,
                              'cart_product_form': cart_product_form})

def Registrate(request):
	if request.method == 'POST':
		formSelect = RegistrateForm(request.POST or None)
		if formSelect.is_valid():
			username = formSelect.cleaned_data['login']
			password1 = formSelect.cleaned_data['password']
			password2 = formSelect.cleaned_data['confirm_password']
			user = User.objects.filter(username = username).count()
			if user == 0:
				if password1 == password2:
					user = User.objects.create_user(username=username)
					user.set_password(password1)
					user.save()
					messages.add_message(request, messages.INFO, "True")
					return redirect('shop:Registrated')
				else:
					messages.add_message(request, messages.INFO, "Password not match!")
					return redirect('shop:Registrate')
			else:
					messages.add_message(request, messages.INFO, "User already exist!")
					return redirect('shop:Registrate')

	else:
		formSelect = RegistrateForm()
		return render(request, 'shop/product/registrate.html', {'form_select': formSelect})



def Registrated(request):

	return render(request,'shop/product/registrated.html')