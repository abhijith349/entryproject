from django.urls import path
from.import views

urlpatterns=[
    path('',views.home,name="home"),
    path('accounts/login/',views.loginview,name="login"),
    path('accounts/sign_up/',views.sign_up,name='signup'),
    path('logout',views.logout_view),
    path('enter',views.enterdetails),
    path('display',views.productinfo),
    path('del',views.delproduct),
    path('update',views.updatename)
]
