from django.contrib import admin
from django.urls import path
from Web.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('del/<todo_id>', delete,name='del'),
]
