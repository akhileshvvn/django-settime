from django.conf.urls import url,include
from . import views


app_name = 'syat'


urlpatterns = [
    url(r'^form/$',views.fill, name = 'fillform'),
    url(r'^error/$',views.error,name='error'),
    url(r'^book/$',views.book,name='book'),
]