from django.urls import path
from .views import home,create,update,delete

urlpatterns = [
    path('',home,name="read"),
    path('student-create/',create,name="create"),
    path('student-update/<int:id>',update,name="update"),
    path('student-delete/<int:id>',delete,name="delete")
]