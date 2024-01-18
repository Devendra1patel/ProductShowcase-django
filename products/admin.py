from django.contrib import admin
from .models import Product
from .models import myContact
from .models import myImages
from .models import about

# Register your models here.
admin.site.register(Product)
admin.site.register(myContact)
admin.site.register(myImages)
admin.site.register(about)

  