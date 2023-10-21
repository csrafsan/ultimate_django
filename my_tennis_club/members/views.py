# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def member(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def detail(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
  
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

# def home(request):
#     return HttpResponse("This is home page")

# def about(request):
#     return HttpResponse("This is about page")
# def contact(request):
#     return HttpResponse("This is contact us page")
# def pricing(request):
#     return HttpResponse("This is pricing page")
# def portfolio(request):
#     return HttpResponse("This is portfolio page")


