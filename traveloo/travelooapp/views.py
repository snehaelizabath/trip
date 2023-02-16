from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Place, Person




def demo(request):
  obj = Place.objects.all()
  objects = Person.objects.all()

  return render(request, "index.html",{'result':obj,'results':objects})

#
#
# def demo(request,c_slug=None):
#     c_page=None
#     products_list=None
#     if c_slug!=None:
#         c_page=get_object_or_404(Person,slug=c_slug)
#         products_list=Place.objects.all().filter(category=c_page,available=True)
#     return render(request, 'index.html',{'results': Person})
#

