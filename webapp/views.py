from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from .models import *

class HomeView(View):
	def get(self,request):
		return render(request, 'webapp/home.html', {})

class ServicesView(View):
	def get(self,request):
		services = Service.objects.all()
		return render(request, 'webapp/services.html', {'services':services})

class PortfolioView(View):
	def get(self,request):
		portfolios = Portfolio.objects.all()
		return render(request, 'webapp/portfolio.html', {'portfolios':portfolios})

class ContactView(View):
	errors = []
	def get(self,request):
		return render(request, 'webapp/contact.html', {'errors': self.errors})
	def post(self,request):
		name = ''
		email = None
		message = None
		if request.POST.get('name'):
			name = request.POST['name']
		if request.POST.get('email'):
			email = request.POST['email']
		else:
			self.errors.append("Email is required.")
		if request.POST.get('message'):
			message = request.POST['message']
		else:
			self.errors.append("Message is required.")

		if not self.errors:
			contact = Contact.objects.create(email=email,full_name=name,message=message)
			messages.info(request, "Feedback sent sucessfully")
		return redirect('/contact')