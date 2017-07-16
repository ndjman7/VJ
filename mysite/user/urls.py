from django.conf.urls import url
from . import views

app_name = 'user'
urlpatterns = [
    url(r'^login$', views.vj_login, name='login'),
    url(r'^logout$', views.vj_logout, name='logout'),
    url(r'^signup$', views.vj_signup, name='signup'),
]
