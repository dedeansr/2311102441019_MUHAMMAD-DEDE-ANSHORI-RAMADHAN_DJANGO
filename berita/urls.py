
from django.urls import path
from berita.views import (
    dashboard,
    kategori_list, kategori_add, kategori_update, kategori_delete,
    artikel_list, artikel_add
    )

urlpatterns = [ 

    path('', dashboard, name="dashboard"),
    path('kategori/list', kategori_list, name="kategori_list"),
    path('kategori/add', kategori_add, name="kategori_add"),
    path('kategori/update/<int:id_kategori>', kategori_update, name="kategori_update"),
    path('kategori/delete/<int:id_kategori>', kategori_delete, name="kategori_delete"),

    path('artikel/list', artikel_list, name="artikel_list"),
    path('artikel/add', artikel_add, name="artikel_add"),

]
