from django.urls import path
from .views import *

urlpatterns = [
    path('view_all_add/', user_all_view_create.as_view()),
    path('view_id_up_de/<int:pk>/', user_all_id_update_delete.as_view()),
]
