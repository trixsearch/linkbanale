from django.urls import path
from .views import (index,detail,redirectToUrl)

urlpatterns = [
    path('',index,name="index"),
    path('detail/<int:id>/',detail,name="detail"),
    path('redirect/<str:shortUrl>/',redirectToUrl,name="redirectToUrl"),
]
