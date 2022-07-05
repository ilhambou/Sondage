from xml.etree.ElementInclude import include
from django.urls import URLPattern, path , include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/',views.registration_view , name = 'register'),
    path('logout/',views.logout_view, name="logout"),
    path('login/',views.login_view, name="login"),
    path('profil/',views.profil_view,name="profil"),
    path('account/',views.account_view,name="account"),
    path('show_users/',views.show_users,name="show_users"),
    path('account_delete/<id>',views.account_delete,name="account_delete"),

    
    
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password/password_change.html'), 
        name='password_change'),


]