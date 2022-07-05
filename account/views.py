import email
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from account.forms import RegistrationForm,AccountAuthenticationForm,AccountUpdateForm
from account.models import Account

# Create your views here.


def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			r_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=r_password)
			login(request, account)
			return redirect('index')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'pages/register.html', context)
##################################################

def logout_view(request):
	logout(request)
	return redirect('index')

##################################################

def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("index")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("index")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	
	return render(request, "pages/login.html", context)


#################################################


def profil_view(request):
	
	return render(request,'pages/profil.html')


#################################################

#def account_view(request):
#	return render(request,"pages/account.html")


################################################

def account_view(request):

	if not request.user.is_authenticated:
			return redirect("login")

	context = {}
	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
					"email": request.POST['email'],
					"username": request.POST['username'],
			}
			form.save()
			context['success_message'] = "Updated"
	else:
		form = AccountUpdateForm(

			initial={
					"email": request.user.email, 
					"username": request.user.username,
				}
			)

	context['account_form'] = form


	return render(request, "pages/account.html", context)


#########################################################


def show_users(request):
	show_userss = Account.objects.all()
	context = {
		'show_userss' : show_userss
	}

	return render(request, "pages/show_users.html",context)
	

#########################################################


def account_delete(request,id):
	account_delete = Account.objects.get(id=id)
	account_delete.delete()
	return redirect('show_users')
