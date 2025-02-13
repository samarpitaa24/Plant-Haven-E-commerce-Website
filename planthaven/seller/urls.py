from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_prod , name="add-product"),
    path("update_data/<int:id>",views.update_data, name="update-data"),
    path("delete_data/<int:id>",views.delete_data, name="deletedata"),
]
