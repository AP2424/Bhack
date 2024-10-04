from django.urls import path, include
from .views import mainpage, videorec_page



urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('student/<str:sname>', videorec_page, name='videorec-page')
]