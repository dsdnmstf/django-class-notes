from operator import index
from django.urls import path
from .views import index,student_detail, student_add, student_delete, student_list, student_update

urlpatterns = [
    path("", index, name="index"),
    path("list/", student_list, name="list"),
    path("add/", student_add, name="add"),
    path("detail/<int:id>", student_detail, name="detail"),
    path("update/<int:id>", student_update, name="update"),
    path("delete/<int:id>", student_delete, name="delete"),
]