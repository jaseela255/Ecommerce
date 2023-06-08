from . import views
from django.urls import path,include

app_name='shop'

urlpatterns = [
    
    path('',views.all_procat,name='all_prodcat'),
    path('<slug:c_slug>/',views.all_procat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodetail,name='prodcatdetail'),

]
