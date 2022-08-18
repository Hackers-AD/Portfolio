from django.urls import path
from .views import *

urlpatterns = [
	path('', HomeView.as_view()),path('home', HomeView.as_view()), path('about', HomeView.as_view()),
	path('services', ServicesView.as_view()),
	path('portfolio', PortfolioView.as_view()),
	path('contact', ContactView.as_view())
]