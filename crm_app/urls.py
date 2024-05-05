
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    # path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('register/', register, name='register'),
    path('record/<int:pk>', customer_record, name='customer_record'),
    path('delete_record/<int:pk>', delete_record, name='delete_record'),
    path('add_record/', add_record, name='add_record'),
    path('update_record/<int:pk>', update_record, name='update_record'),
]
