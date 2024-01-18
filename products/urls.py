from django.conf import settings
from django.conf.urls.static import static


from django.urls import path
from products import views
app_name = 'products'

urlpatterns = [
    path('collection/',views.proView,name="collection"),
    path('mycontact/',views.mycontact,name='connections'),
    path('about/',views.about,name='about'),
    path('detail/<int:id>',views.detail, name='detail'),
    path('test/',views.test)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

