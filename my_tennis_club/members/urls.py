from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.member, name='member'),
    path('members/details/<int:id>', views.detail, name='details'),
    path('testing/', views.testing, name='testing')    
    # path('home/', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('pricing/', views.pricing, name='pricing'),
    # path('portfolio/', views.portfolio, name='portfolio')
]
