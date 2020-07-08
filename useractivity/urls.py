from . import views
from django.urls import path, re_path
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

app_name = 'useractivity'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    re_path(r'^favicon\.ico$', favicon_view),

]
