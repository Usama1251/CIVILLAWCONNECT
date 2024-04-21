from django.urls import path
from app.views import *

urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('lawyer/', L_Home.as_view(), name="Lawyer_home"),
    path('civilian/', C_Home.as_view(), name="Civilian_home"),  # Corrected view name and URL pattern name
    path('create_p/', Create_P.as_view(), name="Create your Profile"),
    path('login_p/', Login_P.as_view(), name="Login your Profile"),
    path('logout/', Logout.as_view(), name="Logout"),
]
