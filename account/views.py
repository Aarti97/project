from django.shortcuts import  render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from account.forms import NewUserForm,CustomerForm,FeedbackForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages #import messages
from django.contrib.auth.forms import AuthenticationForm
from account.models import Customer,Feedback



def sample(request):
	if request.method == "POST":
		form= FeedbackForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect("sample")
			except:
				pass
	else:
		form= FeedbackForm()
	return render(request,'sample.html',{'form':form})



def registerPage(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="register.html", context={"form":form})

def loginPage(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password1 = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password1)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("sample")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"form":form})

def logout_user(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("sample")

def index(request):
	if request.method == "POST":
		form= CustomerForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect("sample")
			except:
				pass
	else:
		form= CustomerForm()
	return render(request,'index.html',{'form':form})