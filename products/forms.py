from django import forms
from .models import Product
from .models import myContact
from .models import myImages

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

class myContact(forms.ModelForm):
    class Meta:
        model = myContact 
        fields = ['serial_no','number', 'name', 'address', 'company', 'order']

class myImagesForm(forms.ModelForm):
    class Meta:
        model = myImages
        fields = ['image','time']