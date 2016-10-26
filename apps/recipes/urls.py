from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.splash, name='splash'),
    url(r'^my_account/$', views.myaccount, name='myaccount'),
    url(r'^add_recipe/$', views.add_recipe, name='add_recipe'),
    url(r'^create_recipe/$', views.create_recipe, name='create_recipe'),
    url(r'^init$', views.first_time, name='first'),
    url(r'^new$', views.new, name='new'),
    url(r'^user/(?P<u_id>\d+)$', views.user, name='userrecipes')
    ]