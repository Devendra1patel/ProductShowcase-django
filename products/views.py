from django.shortcuts import render
from django.http import HttpResponse
# from django.views.generic.detail import DetailView
from .models import Product
from .models import myContact as myContact_model
from .models import myImages as myImages_model
from .models import about as about_model
from .forms import ProductForm
from .forms import myContact 
from .forms import myImagesForm
# Create your views here.
def test(req):
    # s = '<h1>This is my file</h1>'
    return render(req, 'img2.html')

def proView(req):
    # model = Product
    # template_name = 'products/product_detail.html'
    # context_object_name = 'product'
    if req.method == "POST":
        form = ProductForm(req.POST, req.FILES)
        if form.is_valid():
         form.save()
    form = ProductForm
    img = Product.objects.all()
    return render(req, 'img2.html', {'img':img, 'form':form})

def mycontact(req):
   if req.method == "POST":
      form = myContact(req.POST, req.FILES)
      if form.is_valid():
        form.save()
   form = myContact
   contacts = myContact_model.objects.all()
   return render(req, 'numCollection.html',{'contacts':contacts,'form':form})

def about(req):
   if req.method == "POST":
      form = myImagesForm(req.POST, req.FILES )
      if form.is_valid():
         form.save()
   form = myImagesForm
   images = myImages_model.objects.all()
   about_data = about_model.objects.all()
   return render(req, 'about.html',{'images':images,'form':form,"about":about_data[0] })

def detail(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'prod_des.html',{'id':id,'product':product})



