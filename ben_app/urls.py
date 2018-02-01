from django.conf.urls import url
from ben_app import views

app_name = 'ben_app'

urlpatterns = [
   url(r'^$',views.index,name='index'),
   url(r'^about/$',views.about,name='about'),

]
