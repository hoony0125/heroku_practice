from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_view,name="login"),   #두번째 인자는 함수명 
    path('logout/',logout_view,name="logout"),
    path('register/',register_view,name="signup"),
]