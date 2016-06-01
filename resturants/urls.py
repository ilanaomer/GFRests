from django.conf.urls import url

from . import views

app_name = "resturants"
urlpatterns = [
    url(r'^all/$', views.IndexView.as_view(), name="all"),
    url(r'^(?P<pk>[0-9]+)/$', views.ResturantView.as_view(), name='rest_detail'),
]
